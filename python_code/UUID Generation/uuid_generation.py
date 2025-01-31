"""
Understanding UUID - Universally Unique Identifier, to generate random ids.
"""

import uuid

# Generate a UUID from a host ID, sequence number, and the current time
print("uuid 1: ",uuid.uuid1())

# Generate a UUID from the MD5 hash of a namespace UUID and a name.
print("uuid 3: ",uuid.uuid3(uuid.NAMESPACE_DNS,"www.moolya.com"))

# Generate a random UUID. (most common)
print("uuid 4: ",uuid.uuid4())

# Generate a UUID from the SHA-1 hash of a namespace UUID and a name.
print("uuid 5: ",uuid.uuid5(uuid.NAMESPACE_DNS,"www.moolya.com"))

# Generate a UUID as a string without - dashes.
print("UUID as Hex String: ", uuid.uuid4().hex)

