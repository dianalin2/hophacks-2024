import React, { useState } from 'react';
import { Document, Page, pdfjs } from 'react-pdf';

const PDFviewer = () => {
    pdfjs.GlobalWorkerOptions.workerSrc = new URL(
        'pdfjs-dist/build/pdf.worker.min.mjs',
        import.meta.url,
      ).toString();
    const [selectedFile, setSelectedFile] = useState(null);
    const [numPages, setNumPages] = useState(null);
    const [pageNumer, setPageNumer] = useState(1);
    const [pdfData, setPdfData] = useState(null);

    const onFileLoad = (event) => {
        const file = event.target.files[0];
        const reader = new FileReader();

        reader.onload = (e) => {
            setPdfData(e.target.result);
        };

        reader.readAsDataURL(file);
        setSelectedFile(file);
    };

    const onDocumentLoadSuccess = ({ numPages}) => {
        setNumPages(numPages);
    };

    return (
        <div>
            <input type="file" accept = ".pdf" onChange={onFileLoad}/>
            {pdfData && (
                <Document file={pdfData} onLoadSuccess={onDocumentLoadSuccess}>
                    <Page pageNumber={pageNumer}/>
                </Document>
            )}

            {pdfData && (
                <p>Page {pageNumer} of {numPages}</p>
            )}
        </div>
    );
};

export default PDFviewer;