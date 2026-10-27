class SpesifikasiHardware:
    """Objek komponen untuk Komposisi dalam Server."""

    def __init__(self, cpu, ram_gb, tipe_storage):
        self.cpu = cpu                      # Contoh: "AMD EPYC 7763 16-Core"
        self.ram_gb = ram_gb                # Contoh: 64
        self.tipe_storage = tipe_storage    # Contoh: "NVMe SSD"

    def __str__(self):
        return f"{self.cpu} | {self.ram_gb} GB RAM | {self.tipe_storage}"
