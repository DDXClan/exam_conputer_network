def encode_signal(signal, encoding_method):
    encoded_signal = ""
    if encoding_method == "NRZI":
        prev_bit = "0"
        for bit in signal:
            if bit == "1":
                encoded_signal += "0" if prev_bit == "1" else "1"
                prev_bit = encoded_signal[-1]
            else:
                encoded_signal += prev_bit

    elif encoding_method == "AMI":
        prev_bit = "0"
        polarity = 1
        for bit in signal:
            if bit == "1":
                encoded_signal += str(polarity)
                polarity *= -1
            else:
                encoded_signal += prev_bit

    elif encoding_method == "Bipolar":
        prev_bit = "0"
        for bit in signal:
            if bit == "1":
                encoded_signal += "1" if prev_bit == "0" else "-1"
                prev_bit = encoded_signal[-1]
            else:
                encoded_signal += "0"

    elif encoding_method == "Manchester":
        for bit in signal:
            encoded_signal += "01" if bit == "1" else "10"

    elif encoding_method == "2B1Q":
        prev_bits = "00"
        for bit in signal:
            if bit == "1":
                encoded_signal += "11" if prev_bits == "00" or prev_bits == "11" else "00"
            else:
                encoded_signal += "01" if prev_bits == "00" or prev_bits == "01" else "10"
            prev_bits = encoded_signal[-2:]

    return encoded_signal