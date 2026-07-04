def scan_doc(scan_type, input_value, risk, reasons):
    return {
        "type": scan_type,
        "input": input_value,
        "risk": risk,
        "reasons": reasons
    }
