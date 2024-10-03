import hmac
import hashlib
import base64

# Provided Variables
signatureObject = {
    "accountNumber": "3005111131675",
    "amount": "3999",
    "currency": "TZS",
    "reference": "W44FF6F5F6D4A",
    "withdrawToOwnNumber": True,  # Ensure True/False are treated correctly
}

reference = "W44FF6F5F6D4A"

def create_transaction_signature(reference, input_string):
    # Generate the final HMAC signature
    return generate_hmac_signature_sha256(reference, input_string)

def generate_hmac_signature_sha256(key, input_string):
    # Encode the key to bytes
    key_bytes = key.encode('utf-8')

    # Create HMAC object with the key and input string
    hmac_obj = hmac.new(key_bytes, input_string.encode('utf-8'), hashlib.sha256)

    # Return the HMAC signature encoded in base64
    return base64.b64encode(hmac_obj.digest()).decode('utf-8')

def generate_hmac_signature(input_string, reference):
    # Create the HMAC signature using SHA-256 and return it
    return create_transaction_signature(reference, input_string)

def generate_signature(signature_object, reference):
    # Step 1: Concatenate the values with '&'
    # Convert boolean to lowercase string
    signature = '&'.join(
        str(value).lower() if isinstance(value, bool) else str(value)
        for value in signature_object.values()
    )

    # Step 2: Generate the HMAC signature
    sig = generate_hmac_signature(signature, reference)
    return sig

# Generate the signature using the provided data
signature = generate_signature(signatureObject, reference)
print("Generated Signature:", signature)
