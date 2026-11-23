# ==========================================
# CODSOFT AI INTERNSHIP
# TASK 3 - IMAGE CAPTIONING AI
# ==========================================

import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from tkinter import Tk, filedialog


def image_captioning():

    print("=" * 50)
    print("          IMAGE CAPTIONING AI")
    print("=" * 50)

    # Select image
    root = Tk()
    root.withdraw()

    image_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[
            ("Image Files", "*.jpg *.jpeg *.png *.webp")
        ]
    )

    root.destroy()

    if not image_path:
        print("No image selected!")
        return

    try:
        print("\nLoading AI model...")
        print("Please wait...")

        # Select device
        device = "cuda" if torch.cuda.is_available() else "cpu"

        # Load pretrained BLIP model
        processor = BlipProcessor.from_pretrained(
            "Salesforce/blip-image-captioning-base"
        )

        model = BlipForConditionalGeneration.from_pretrained(
            "Salesforce/blip-image-captioning-base"
        )

        model.to(device)
        model.eval()

        # Open image
        image = Image.open(image_path).convert("RGB")

        # Process image
        inputs = processor(
            images=image,
            return_tensors="pt"
        ).to(device)

        # Generate caption
        with torch.no_grad():
            output = model.generate(
                **inputs,
                max_new_tokens=50
            )

        caption = processor.decode(
            output[0],
            skip_special_tokens=True
        )

        # Display result
        print("\n" + "=" * 50)
        print("             GENERATED CAPTION")
        print("=" * 50)
        print("Image:", image_path)
        print("Caption:", caption)
        print("=" * 50)

        # Show selected image
        image.show()

    except Exception as error:
        print("\nError:", error)


if __name__ == "__main__":
    image_captioning()
    
