from adobe.pdfservices.operation.auth.credentials import Credentials
from adobe.pdfservices.operation.client_config import ClientConfig
from adobe.pdfservices.operation.exception.exceptions import ServiceApiException, ServiceUsageException, SdkException
from adobe.pdfservices.operation.execution_context import ExecutionContext
from adobe.pdfservices.operation.io.file_ref import FileRef
from adobe.pdfservices.operation.pdfops.extract_pdf_operation import ExtractPDFOperation
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_pdf_options import ExtractPDFOptions
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_element_type import (
    ExtractElementType
)
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_renditions_element_type import (
    ExtractRenditionsElementType
)
from adobe.pdfservices.operation.pdfops.options.extractpdf.table_structure_type import TableStructureType

import os.path
import zipfile
import json
import logging


# Get the samples from http://www.adobe.com/go/pdftoolsapi_python_sample
# Run the sample:
# python src/extractpdf/extract_txt_table_info_from_pdf.py

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

try:

    # Initial setup, create credentials instance.
    credentials = Credentials.service_principal_credentials_builder()\
        .with_client_id('0c9f5463c71048c08c022904a30f786c')\
        .with_client_secret('p8e-mAtSx1ILy2d15uSftBBiSFT4XwksEk3H')\
        .build()

    # Create client config instance with custom time-outs.
    client_config = ClientConfig.builder().with_connect_timeout(10000).with_read_timeout(40000)\
        .build()

    # Create an ExecutionContext using credentials and create a new operation
    # instance.
    # Create an ExecutionContext using credentials and create a new operation instance.
    execution_context = ExecutionContext.create(credentials, client_config)
    extract_pdf_operation = ExtractPDFOperation.create_new()

    # Set operation input from a source file.
    # source = FileRef.create_from_local_file("./resources/盐湖股份2023年半年度业绩预告-2023-07-15.pdf")
    # source = FileRef.create_from_local_file("./resources/foo.pdf")
    # source = FileRef.create_from_local_file("./resources/sec_example.pdf")
    source = FileRef.create_from_local_file("./resources/test1.pdf")
    extract_pdf_operation.set_input(source)

    # Build ExtractPDF options and set them into the operation
    extract_pdf_options: ExtractPDFOptions = ExtractPDFOptions.builder() \
        .with_element_to_extract(ExtractElementType.TEXT) \
        .with_element_to_extract(ExtractElementType.TABLES) \
        .with_element_to_extract_renditions(ExtractRenditionsElementType.TABLES) \
        .with_element_to_extract_renditions(ExtractRenditionsElementType.FIGURES) \
        .with_get_char_info(True) \
        .with_include_styling_info(True) \
        .with_table_structure_format(TableStructureType.CSV) \
        .build()
    extract_pdf_operation.set_options(extract_pdf_options)

    # Execute the operation.
    result: FileRef = extract_pdf_operation.execute(execution_context)

    # Save the result to the specified location.
    # result.save_as("./output/盐湖股份2023年半年度业绩预告-2023-07-15.zip")
    # result.save_as("./output/foo.zip")
    # result.save_as("./output/sec_example.zip")
    result.save_as("./output/test1.zip")

except (ServiceApiException, ServiceUsageException, SdkException):
    logging.exception("Exception encountered while executing operation")
