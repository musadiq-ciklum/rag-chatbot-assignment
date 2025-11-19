import os

FOLDERS = [
    "data/raw/slides",
    "data/raw/audio",
    "data_outputs/transcripts",
    "data_outputs/chunks",
    "data_outputs/embeddings",
]

def ensure_dir(path: str):
    """Create directory if it doesn't exist."""
    os.makedirs(path, exist_ok=True)

def ensure_gitkeep(path: str):
    """Create .gitkeep file so Git tracks an empty folder."""
    gitkeep_path = os.path.join(path, ".gitkeep")
    if not os.path.exists(gitkeep_path):
        with open(gitkeep_path, "w", encoding="utf-8"):
            pass  # Create empty file

def main():
    print("\n📂 Setting up project folder structure...\n")

    for folder in FOLDERS:
        ensure_dir(folder)
        ensure_gitkeep(folder)
        print(f"✓ Created: {folder}")

    print("\n🎉 Project setup complete!")
    print("\nNext steps:")
    print("1️⃣ Place your PDF files inside:")
    print("    → data/raw/slides/")
    print("2️⃣ Place your audio/video files inside:")
    print("    → data/raw/audio/")
    print("\n3️⃣ Run PDF extraction:")
    print("    python -m src.pdf_processing.extract_pdf "
          "--pdf-path data/raw/slides/YourFile.pdf "
          "--out-dir data_outputs/transcripts")
    print("\n4️⃣ Continue with audio transcription (next feature).")
    print("\nDone!\n")

if __name__ == "__main__":
    main()
