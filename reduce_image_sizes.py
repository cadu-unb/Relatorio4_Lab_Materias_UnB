import os
from io import BytesIO
from pathlib import Path

from PIL import Image

# Maximum size in bytes (250 KB)
MAX_BYTES = 250 * 1024

# Extensions we treat as images
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff"}


def is_image_file(path: Path) -> bool:
    return path.suffix.lower() in IMAGE_EXTENSIONS


def reduce_image(input_path: Path, max_bytes: int = MAX_BYTES) -> None:
    """
    Create a reduced-size version of `input_path` named
    `reduced_<original_name><ext>` in the same folder.
    Tries to keep file size <= max_bytes.
    """
    output_path = input_path.with_name(f"reduced_{input_path.name}")

    # Skip if the reduced file already exists
    if output_path.exists():
        print(f"[SKIP] {output_path} already exists")
        return

    try:
        img = Image.open(input_path)
    except Exception as e:
        print(f"[ERROR] Cannot open {input_path}: {e}")
        return

    # Preserve original format if possible
    img_format = img.format or input_path.suffix.replace(".", "").upper()

    # Ensure mode is compatible with saving
    if img_format.upper() in ("JPEG", "JPG") and img.mode not in ("RGB", "L"):
        img = img.convert("RGB")

    quality = 95
    width, height = img.size

    # We'll iteratively compress and, if needed, resize
    while True:
        buffer = BytesIO()

        save_kwargs = {}
        fmt = img_format.upper()

        if fmt in ("JPEG", "JPG"):
            save_kwargs.update({"quality": quality, "optimize": True})
        elif fmt == "WEBP":
            save_kwargs.update({"quality": quality})
        elif fmt == "PNG":
            # For PNG, we can't use "quality", but we can optimize
            save_kwargs.update({"optimize": True, "compress_level": 9})
        # For other formats, just save with default options

        try:
            img.save(buffer, format=fmt, **save_kwargs)
        except OSError:
            # Some formats might not support certain params; retry with defaults
            buffer = BytesIO()
            img.save(buffer, format=fmt)

        size = len(buffer.getvalue())

        if size <= max_bytes:
            # Success: write to output
            with open(output_path, "wb") as f:
                f.write(buffer.getvalue())
            print(f"[OK] {input_path} -> {output_path} ({size/1024:.1f} KB)")
            return

        # If we get here, it's still too big. Try to reduce further.
        # Strategy:
        # 1) For JPEG/WEBP: first lower quality down to 30.
        # 2) If still too big (or non-JPEG/WEBP), downscale the image by 10% steps.
        resized = False

        if fmt in ("JPEG", "JPG", "WEBP") and quality > 30:
            quality -= 5
        else:
            # Resize down by 10%
            new_width = int(width * 0.9)
            new_height = int(height * 0.9)

            # If image is already very small, stop trying
            if new_width < 200 or new_height < 200:
                # Save best effort and warn
                with open(output_path, "wb") as f:
                    f.write(buffer.getvalue())
                print(
                    f"[WARN] Could not reduce {input_path} below {max_bytes/1024:.0f} KB. "
                    f"Final size: {size/1024:.1f} KB"
                )
                return

            img = img.resize((new_width, new_height), Image.LANCZOS)
            width, height = img.size
            resized = True

        if not resized and quality <= 30:
            # If we are here, quality is already low and we couldn't resize (e.g. format),
            # so we will try resizing anyway.
            new_width = int(width * 0.9)
            new_height = int(height * 0.9)
            if new_width < 200 or new_height < 200:
                with open(output_path, "wb") as f:
                    f.write(buffer.getvalue())
                print(
                    f"[WARN] Could not reduce {input_path} below {max_bytes/1024:.0f} KB. "
                    f"Final size: {size/1024:.1f} KB"
                )
                return
            img = img.resize((new_width, new_height), Image.LANCZOS)
            width, height = img.size


def main():
    # Root folder = folder where this script is located
    root_dir = Path(__file__).resolve().parent

    print(f"Scanning from root: {root_dir}")
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirpath = Path(dirpath)
        for filename in filenames:
            path = dirpath / filename

            # Skip already reduced images
            if path.name.startswith("reduced_"):
                continue

            if is_image_file(path):
                print(f"[PROCESS] {path}")
                reduce_image(path)


if __name__ == "__main__":
    main()
