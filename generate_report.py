from fpdf import FPDF
import os
from datetime import datetime

def create_pdf_report(results, screenshots_folder="screenshots", report_folder="reports"):
    os.makedirs(report_folder, exist_ok=True)

    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    pdf_filename = f"{report_folder}/report_{now}.pdf"

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    for result in results:
        pdf.add_page()

        test_name = result["test_name"]
        status = result["status"]
        screenshot = result["screenshot"]

        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, f"Scenario: {test_name}", ln=True)
        pdf.set_font("Arial", "B", 12)
        
        if status == "PASS":
            r, g, b = 0, 128, 0 # green        
        else:
            r, g, b = 200, 0, 0 # red
        pdf.set_text_color(r, g, b)        
        pdf.cell(0, 10, f"Status: {status}", ln=True)
        pdf.set_text_color(0,0,0)   
        

        if os.path.exists(os.path.join(screenshots_folder, screenshot)):
            pdf.image(os.path.join(screenshots_folder, screenshot), w=180)
        else:
            pdf.cell(0, 10, "Screenshot não encontrada.", ln=True)

    pdf.output(pdf_filename)
    print(f"\nPDF salvo em: {pdf_filename}")