from collections import namedtuple


DataIngestionArtifact = namedtuple("DataIngestionArtifact", ["train_file_path","test_file_Path", "is_ingested", "message"])