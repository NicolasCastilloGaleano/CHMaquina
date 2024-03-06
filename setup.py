from distutils.core import setup
import py2exe

setup(console=['main.py'],data_files=[('src/front/img', ['src/front/img/pantalla.png', 'src/front/img/impresora.png'])],)
