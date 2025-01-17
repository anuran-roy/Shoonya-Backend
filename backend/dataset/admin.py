from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .resources import *
from .models import *


class DatasetInstanceAdmin(ImportExportActionModelAdmin):
    resource_class = DatasetInstanceResource


admin.site.register(DatasetInstance, DatasetInstanceAdmin)

### Dataset types ###

# TODO: Find a clean generic way to do this:
class SentenceTextAdmin(ImportExportActionModelAdmin):
    resource_class = SentenceTextResource


class TranslationPairAdmin(ImportExportActionModelAdmin):
    resource_class = TranslationPairResource


class OCRDocumentAdmin(ImportExportActionModelAdmin):
    resource_class = OCRResource


class BlockTextAdmin(ImportExportActionModelAdmin):
    resource_class = BlockTextResource


admin.site.register(SentenceText, SentenceTextAdmin)
admin.site.register(TranslationPair, TranslationPairAdmin)
admin.site.register(OCRDocument, OCRDocumentAdmin)
admin.site.register(BlockText, BlockTextAdmin)
