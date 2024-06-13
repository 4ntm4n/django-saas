import helpers
from django.conf import settings
from django.core.management import BaseCommand

STATICFILES_VENDOR_DIR = getattr(settings, 'STATICFILES_VENDOR_DIR')

VENDOR_STATICFILES = {
    "flowbite.min.css" : "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.css",
    "flowbite.min.js" : "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js"
}

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.stdout.write("dowloading vendor files...")
        completed_urls = []
        for name, url in VENDOR_STATICFILES.items():
            out_path = STATICFILES_VENDOR_DIR / name
            dl_sucess = helpers.download_to_local(url, out_path)
            if dl_sucess:
                completed_urls.append(url)
                self.stdout.write(f"{name} downloaded successfully.")
            else:
                self.stdout.write(
                    self.style.ERROR(f"{name} did not dowload correctly")
                )
        if set(completed_urls) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(
                self.style.SUCCESS(
                    "All vendor files downloaded successfully."
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING(
                    "Some vendor files did not download correctly."
                )
            )