import fitz  # PyMuPDF


def extract_text_and_layout_from_pdf(pdf_path):
    try:
        # Open the PDF file
        pdf_document = fitz.open(pdf_path)

        text_blocks = []
        # Iterate through the pages
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            blocks = page.get_text("blocks")

            print(f"Page {page_num + 1} Blocks: {blocks}")  # Debug: print blocks

            for block in blocks:
                # Print block type for debugging
                print(f"Block: {block}")
                if isinstance(block, (tuple, list)):
                    if len(block) == 4:
                        block_type, bbox, text, _ = block
                        text_blocks.append({"type": block_type, "bbox": bbox, "text": text})
                    elif len(block) == 5:
                        block_type, bbox, text, _, _ = block
                        text_blocks.append({"type": block_type, "bbox": bbox, "text": text})
                    else:
                        # Handle other cases or log them for further analysis
                        print(f"Unexpected block format: {block}")

        return text_blocks

    except Exception as e:
        print(f'Error extracting text and layout from PDF: {e}')
        return []
