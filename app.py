import sys
import os
import tempfile
import struct
import brotli
from PIL import Image
import io
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QMenuBar, QMenu, QAction, QFileDialog, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QDialog
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QFileInfo, QRectF

# XOR şifreleme fonksiyonu
def xor_sifrele(veri, anahtar=0xAA):
    return bytearray([byte ^ anahtar for byte in veri])

# Resmi WebP formatında kaydedip XOR şifreleme ile sıkıştırarak .xtend dosyasına kaydetme
def resimden_xtend_olustur(resim_yolu, xtend_dosyasi):
    try:
        # Resmi açma ve RGBA formatına dönüştürme (şeffaflık için)
        img = Image.open(resim_yolu)
        img = img.convert('RGBA')  # Şeffaflık (Alfa Kanalı) korunacak
        
        # Resim boyutlarını al
        width, height = img.size
        
        # Resmi WebP formatında kaydetme (şeffaflık destekleyen format)
        with io.BytesIO() as output:
            img.save(output, format="WEBP", lossless=True, quality=100)
            webp_data = output.getvalue()
        
        # XOR şifrelemesi
        sifrelenmis_veri = xor_sifrele(webp_data)
        
        # Veriyi Brotli ile sıkıştırma
        sıkıştırılmış_veri = brotli.compress(sifrelenmis_veri)
        
        # Veriyi dosyaya kaydetme
        with open(xtend_dosyasi, "wb") as f:
            f.write(struct.pack('ii', width, height))  # Boyutları kaydedin
            f.write(sıkıştırılmış_veri)
        
        print(f".xtend dosyası başarıyla oluşturuldu: {xtend_dosyasi}")
    
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hakkında")
        self.setGeometry(100, 100, 500, 350)  # Genişliği artırdık
        
        # Logo görseli
        logo_label = QLabel(self)
        logo_pixmap = QPixmap("Logo.png")
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignLeft)
        
        # Metin
        about_text = QLabel(self)
        about_text.setText(
            "XTEND Project'in üyesi olan Bekir.00 Discord kullanıcı adıyla bilinen Bekir tarafından hazırlanmıştır.\n\n"
            "İsimler ve görsellerin tüm hakları XTEND Project’e aittir (copyright).\n\n"
            "Kod, dosya yapısı ve diğer tüm bileşenler, Bekir5959 (Bekir.00, Bekir) tarafından CC BY-ND 4.0 lisansı ile lisanslanmıştır.\n"
            "Bu lisans altında türev çalışmalara veya kopya oluşturmaya izin verilmez. Ancak, kodun yazarıyla iletişime geçilerek ve izin alınarak bu işlemler gerçekleştirilebilir.\n"
            ".xtend dosyası'da yapısı gereği Bekir5959 (Bekir.00, Bekir) tarafından CC BY-ND 4.0 lisansı ile lisanslanmıştır.\n"
        )
        about_text.setWordWrap(True)
        about_text.setAlignment(Qt.AlignTop)
        about_text.setStyleSheet("max-width: 450px;")  # Metin genişliğini sınırlandırma (isteğe bağlı)
        
        # Düzenleme
        layout = QVBoxLayout()
        layout.addWidget(logo_label)
        layout.addWidget(about_text)
        
        self.setLayout(layout)


class ImageViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Image Viewer")
        self.setGeometry(100, 100, 800, 600)
        
        self.view = QGraphicsView(self)
        self.scene = QGraphicsScene(self)
        self.view.setScene(self.scene)
        
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)

        # Menü oluşturma
        self.menu_bar = self.menuBar()
        file_menu = self.menu_bar.addMenu("File")
        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_image)
        file_menu.addAction(open_action)

        save_as_action = QAction("Save as .xtend", self)
        save_as_action.triggered.connect(self.save_as_xtend)
        file_menu.addAction(save_as_action)
        
        # About menüsünü ekleme
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)
        help_menu = self.menu_bar.addMenu("Help")
        help_menu.addAction(about_action)

        self.view.setDragMode(QGraphicsView.ScrollHandDrag)

        self.pixmap_item = None
        self.zoom_factor = 1.0
        self.min_zoom = 0.2
        self.max_zoom = 5.0
        self.original_pixmap = None

        # Alt kısımda dosya bilgilerini göstermek için bir label
        self.info_label = QLabel(self)
        self.info_label.setAlignment(Qt.AlignLeft)
        self.info_label.setStyleSheet("color: black; font-size: 12px; padding: 10px;")

        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addWidget(self.info_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        # Uygulama simgesini ayarlama
        self.setWindowIcon(QIcon("Logo.png"))
    
    def wheelEvent(self, event):
        if event.modifiers() == Qt.ShiftModifier:
            delta = event.angleDelta().y()
            if delta > 0:
                self.zoom_in()
            elif delta < 0:
                self.zoom_out()
        else:
            super().wheelEvent(event)
    
    def zoom_in(self):
        if self.zoom_factor < self.max_zoom:
            self.zoom_factor *= 1.1
            self.view.scale(1.1, 1.1)

    def zoom_out(self):
        if self.zoom_factor > self.min_zoom:
            self.zoom_factor /= 1.1
            self.view.scale(0.9, 0.9)
    
    def open_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.jpg *.bmp *.gif *.xtend)")
        if file_path:
            if file_path.endswith(".xtend"):
                self.decode_xtend_image(file_path)
            else:
                self.load_image(file_path)
    
    def load_image(self, file_path):
        pixmap = QPixmap(file_path)
        if pixmap.isNull():
            return
        
        self.original_pixmap = pixmap
        self.pixmap_item = QGraphicsPixmapItem(pixmap)
        self.scene.clear()
        self.scene.addItem(self.pixmap_item)
        self.view.setScene(self.scene)
        self.zoom_factor = 1.0

        # Sahne boyutlarını, görselin boyutlarına göre ayarlıyoruz
        self.view.setSceneRect(QRectF(self.pixmap_item.pixmap().rect()))
        
        # Resim bilgilerini göster
        self.show_image_info(file_path)
    
    def show_image_info(self, file_path):
        file_info = QFileInfo(file_path)
        file_size = file_info.size()
        last_modified = file_info.lastModified().toString()
        
        pixmap = QPixmap(file_path)
        width = pixmap.width()
        height = pixmap.height()

        # Dosya boyutunu KB veya MB cinsinden hesaplayalım
        if file_size < 1024:
            size_str = f"{file_size} B"
        elif file_size < 1024 * 1024:
            size_str = f"{file_size / 1024:.2f} KB"
        else:
            size_str = f"{file_size / (1024 * 1024):.2f} MB"

        info_text = f"Resolution: {width}x{height}\n" \
                    f"Last Modified: {last_modified}\n" \
                    f"Size: {size_str}"

        self.info_label.setText(info_text)
    
    def save_as_xtend(self):
        # Geçici dosyayı Windows temp klasöründe oluştur
        self.temp_file = os.path.join(tempfile.gettempdir(), "temp_image.png")
        
        # Dosya kaydetme penceresini açma
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Image as .xtend", "", ".xtend Files (*.xtend)")
        if file_path:
            if not file_path.endswith(".xtend"):
                file_path += ".xtend"
            
            # Resmi .xtend formatında kaydetme
            if self.original_pixmap:
                self.original_pixmap.save(self.temp_file)
                resimden_xtend_olustur(self.temp_file, file_path)

    def cleanup(self):
        """ Geçici dosyaları temizler """
        if hasattr(self, 'temp_file') and os.path.exists(self.temp_file):
            os.remove(self.temp_file)
            print("Temporary file removed.")
    
    def decode_xtend_image(self, xtend_dosyasi):
        try:
            # .xtend dosyasını çözme işlemi
            temp_decoded_file = os.path.join(tempfile.gettempdir(), "decoded_image.webp")
            with open(xtend_dosyasi, "rb") as f:
                data = f.read()
                width, height = struct.unpack('ii', data[:8])
                compressed_data = data[8:]
                decrypted_data = xor_sifrele(brotli.decompress(compressed_data))

                with open(temp_decoded_file, "wb") as output:
                    output.write(decrypted_data)

            # Çözülmüş resmi yükleme
            self.load_image(temp_decoded_file)
        
        except Exception as e:
            print(f"Bir hata oluştu: {e}")
    
    def show_about(self):
        about_dialog = AboutDialog()
        about_dialog.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageViewer()
    window.show()
    sys.exit(app.exec_())
