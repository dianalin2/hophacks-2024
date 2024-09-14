from fpdf import FPDF, XPos, YPos

def generate_pdf(output_filename, name, age, sex, summary, follow_up, symptoms, possible_diagnoses):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Helvetica", size=14, style="B")
    pdf.cell(0, 15, text=f"Patient Information", align="C", border=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", size=12)
    pdf.cell(pdf.epw / 2, 10, text=f"  **Name**   {name}", align="L", border=True, new_x=XPos.RIGHT, new_y=YPos.LAST, markdown=True)
    pdf.cell(pdf.epw / 4, 10, text=f"  **Age**   {age}", align="L", border=True, new_x=XPos.RIGHT, new_y=YPos.LAST, markdown=True)
    pdf.cell(pdf.epw / 4, 10, text=f"  **Sex**   {sex}", align="L", border=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT, markdown=True)

    pdf.cell(0, 5, text=" ", align="C", border=False, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", size=12, style="B")

    pdf.cell(0, 10, text="Summary", align="C", border=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", size=10)
    pdf.multi_cell(0, 10, summary, border=True, markdown=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT, padding=3)

    pdf.multi_cell(0, 5, text=" ", align="C", border=False, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", size=12, style="B")

    pdf.cell(0, 10, text="Follow-Up Questions", align="C", border=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", size=10)
    for i, (question, answer) in enumerate(follow_up):
        pdf.multi_cell(0, 10, text=f"**{i + 1}. {question}**\n{answer}", border=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT, padding=3, markdown=True)

    pdf.multi_cell(0, 5, text=" ", align="C", border=False, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_font("Helvetica", size=12, style="B")
    pdf.cell(pdf.epw / 2, 10, text="Symptoms", align="C", border=True, new_x=XPos.RIGHT, new_y=YPos.LAST)
    pdf.cell(pdf.epw / 2, 10, text="Possible Diagnoses", align="C", border=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_font("Helvetica", size=10)
    pdf.multi_cell(pdf.epw / 2, 10, text="\n".join(symptoms), align="C", border=True, new_x=XPos.RIGHT, new_y=YPos.TOP, padding=3)
    pdf.multi_cell(pdf.epw / 2, 10, text="\n".join(possible_diagnoses), align="C", border=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT, padding=3)


    pdf.output(output_filename)

if __name__ == "__main__":
    generate_pdf("out/temp.pdf", "John Doe", 25, "M", "This is a summary of the patient's symptoms.", [("Question 1", "wahoowa"), ("Question 2", "ay ay ay")], ["headache", "fever"], ["migraine", "flu"])
