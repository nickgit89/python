import tempfile

temporary = tempfile.TemporaryFile()

temporary.write(b"Save this advice: Keep saving money")
temporary.seek(0)

print(temporary.read())
temporary.close