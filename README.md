# PDF2XL: PDF Bills to Excel Converter

PDF2XL is a powerful application that converts compiled invoices generated from `Delhivery` courier services into a final excel bill. The application is built using Next.js for the frontend and Flask for the backend.
<br />
![image](https://github.com/roboroaster/pdf2xl/assets/75543479/fe9bd106-3c23-40a1-989d-e9cafa3520ea)
<br />
## Project Structure

The project is divided into two main directories:

- `pdf2xl-backend/`: Contains the Flask backend server which handles the PDF to Excel conversion.
- `pdf2xl-frontend/`: Contains the Next.js frontend application which provides a user interface for uploading PDFs and downloading the converted Excel files.

## Backend

The backend is a Flask application that exposes an API endpoint for converting PDF invoices to Excel. It uses libraries such as `pdfminer`, `pdfquery`, and `pdfplumber` for extracting text from PDFs, and `pandas` for creating and writing to Excel files.

The main logic for the conversion is in the `sample_endpoint` function in `app.py`. This function extracts text from the uploaded PDF, parses the text to extract invoice details, and writes these details to an Excel file.

## Frontend

The frontend is a Next.js application that provides a user-friendly interface for uploading PDFs and downloading the converted Excel files. It uses libraries such as `axios` for making API requests to the backend, and `framer-motion`, `tailwindcss` for styling and animations along with `shadcn/ui` and `aceternity ui` for custom components.

The main page of the application is in `app/page.tsx`. This page includes a form for uploading PDFs and a download link for the converted Excel file.

## Getting Started

To setup the backend server:
1. create a virtual environment inside the backend directory:
```bash
python3 -m venv .env
```
2. Install the libraries required inside the virtual environment:
   
```bash
source .env/bin/activate
pip install -r requirements.txt
```
<br />
<br />
To run the backend server, navigate to the `pdf2xl-backend/` directory and run:
<br />

```bash
python app.py
```

The server will start on port `8000`.

To run the frontend application, navigate to the `pdf2xl-frontend/pdf2xl/` directory and run:

```bash
npm run dev
```

The application will start on port `3000`.

## Conclusion

PDF2XL is a powerful tool for converting PDF invoices to Excel, making it easier to manage and analyze invoice data and track your bills. If you're a Delhivery franchise owner wanting to generate a compiled excel bills for their invoices , PDF2XL can save you time and effort in your work.
