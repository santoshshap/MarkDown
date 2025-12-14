
from zipfile import ZipFile, ZIP_DEFLATED
from flask import Flask, request, send_file, render_template_string
from io import BytesIO
from mardownConverter import FORM_TEMPLATE, convert_docx_to_markdown

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template_string(FORM_TEMPLATE)

    # POST: handle form submission
    work_item_number = request.form.get("work_item_number", "").strip()
    language = request.form.get("language", "").strip()
    file = request.files.get("docx_file")

    if not work_item_number or not language or not file:
        return render_template_string(FORM_TEMPLATE, error="All fields are required.")

    language = language.upper()
    work_item_number = work_item_number.upper()

    if not file.filename.lower().endswith(".docx"):
        return render_template_string(FORM_TEMPLATE, error="Please upload a .docx file.")

    docx_bytes = file.read()

    try:
        markdown_text, image_store = convert_docx_to_markdown(docx_bytes, work_item_number, language)
    except Exception as e:
        return render_template_string(FORM_TEMPLATE, error=f"Conversion error: {e}")

    # Build ZIP in-memory
    zip_buf = BytesIO()
    zip_name = f"{work_item_number}.zip"
    md_name = f"{work_item_number}-{language}-{language}.md"

    with ZipFile(zip_buf, "w", ZIP_DEFLATED) as zf:
        # Add markdown
        zf.writestr(md_name, markdown_text)

        # Add images
        for rel_path, data in image_store.items():
            zf.writestr(rel_path, data)

    zip_buf.seek(0)

    return send_file(
        zip_buf,
        as_attachment=True,
        download_name=zip_name,
        mimetype="application/zip",
    )

# --------------------------------------------------
# Entry point
# --------------------------------------------------

if __name__ == "__main__":
    # For local development
    app.run(debug=True)