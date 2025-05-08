import os
from weasyprint import HTML

INVOICE_FOLDER = 'invoices'

def generate_invoice_pdf(user_id, items, total):
    # Build HTML content
    html_content = f"""
    <h1>Invoice for User {user_id}</h1>
    <table border="1" cellpadding="5" cellspacing="0">
        <tr>
            <th>Medicine</th>
            <th>Price</th>
            <th>Quantity</th>
            <th>Subtotal</th>
        </tr>
    """
    for item in items:
        html_content += f"""
        <tr>
            <td>{item['name']}</td>
            <td>${item['price']:.2f}</td>
            <td>{item['quantity']}</td>
            <td>${item['subtotal']:.2f}</td>
        </tr>
        """

    html_content += f"""
        <tr>
            <td colspan="3"><strong>Total</strong></td>
            <td><strong>${total:.2f}</strong></td>
        </tr>
    </table>
    """

    # Generate PDF
    os.makedirs(INVOICE_FOLDER, exist_ok=True)
    invoice_path = os.path.join(INVOICE_FOLDER, f"invoice_user_{user_id}.pdf")
    HTML(string=html_content).write_pdf(invoice_path)
    return invoice_path
