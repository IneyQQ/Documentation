
class CompressionClient:
    @staticmethod
    def get_compress_cmd(path, compression):
        if compression == "tar.gz":
            return ["tar", "-zcf", path+".tar.gz", path]
        if compression == "gz":
            return ["gzip", path]
