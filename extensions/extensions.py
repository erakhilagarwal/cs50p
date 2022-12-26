def main():
    fileName = input("Whats file name: ")
    fileType = getFileTypeFromName(fileName)
    print(f"{fileType}")

def getFileTypeFromName(file):
    file = file.strip().lower()
    name, dot, suffix = file.rpartition(".")
    match(suffix):
        case "gif":
            return "image/gif"
        case "jpg" | "jpeg":
            return "image/jpeg"
        case "png":
            return "image/png"
        case "pdf":
            return "application/pdf"
        case "txt":
            return "text/plain"
        case "zip":
            return "application/zip"
        case _:
            return "application/octet-stream"
    return "application/octet-stream"

main()