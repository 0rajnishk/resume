import subprocess

def pdf_to_image_subprocess(pdf_path, output_path, dpi=200):
    try:
        subprocess.run(
            ["pdftoppm", "-jpeg", "-r", str(dpi), pdf_path, output_path],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
        print(f"Command that failed: {e.cmd}")
        print(f"Error output: {e.output}")

# Example usage
pdf_to_image_subprocess("pdf.pdf", "output", dpi=200)
