import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from tkinter import Tk, filedialog


def image_captioning():

    print("================================")
    print("       IMAGE CAPTIONING AI")
    print("================================")

    # Select an image
    root = Tk()
    root.withdraw()

    image_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[
            ("Image Files", "*.jpg *.jpeg *.png *.bmp")
        ]
    )

    if not image_path:
        print("No image selected!")
        return

    print("\nLoading Image Captioning Model...")
    print("Please wait...")

    try:
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
        print("\n================================")
        print("       GENERATED CAPTION")
        print("================================")
        print(caption)
        print("================================")

        image.show()

    except Exception as error:
        print("\nError:", error)


if __name__ == "__main__":
    image_captioning()
