
function handlePrint() {
    // Trigger the print functionality
    window.print();
}

function handlePrint2() {
    // Select the element you want to convert to PDF
    const element = document.getElementById('page-wrap');

    // Use html2pdf library to generate PDF
    html2pdf(element, {
        margin: 10,
        filename: 'Cthulhu_Resume.pdf',
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: { scale: 2 },
        jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' },
    });
}
document.getElementById('downloadPdf').addEventListener('click', function () {
    var element = document.getElementById('page-wrap'); // HTML sahifasining barcha elementlarini olish
    html2pdf(element); // html2pdf kutubxonasini ishlatib PDF ga o'zgartirib olish
});