import pickle

from PyQt5.QtWidgets import QMainWindow, QDialog, QTableWidgetItem, QFileDialog

from .ui_pap import Ui_MainWindowPAP
from .ui_add_star import Ui_DialogAddStar
from core.data import Data
from core.get_zenith import get_zenith
from core.calc import calc


class PAPWindow(QMainWindow, Ui_MainWindowPAP):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 初始化
        self.data = Data()  # 数据
        self.w = None  # 子窗口，保证生命周期

        # 连接信号与槽
        self.connect()

    def connect(self):
        """连接信号与槽"""
        self.pushButton_add_star.clicked.connect(self.add_star)
        self.pushButton_del_star.clicked.connect(self.del_star)
        self.pushButton_import.clicked.connect(self.import_stars)
        self.pushButton_export.clicked.connect(self.export_stars)
        self.pushButton_browse.clicked.connect(self.browse)
        self.pushButton_calc.clicked.connect(self.calc)

    def update_table(self):
        """更新显示星星的表格和下面的像素焦距"""
        # 更新表格
        self.tableWidget_stars.setRowCount(len(self.data.stars))
        for i, name in enumerate(self.data.stars.keys()):
            star = self.data.stars[name]
            self.tableWidget_stars.setItem(i, 0, QTableWidgetItem(name))
            self.tableWidget_stars.setItem(i, 1, QTableWidgetItem(str(star['coordinate'][0])))
            self.tableWidget_stars.setItem(i, 2, QTableWidgetItem(str(star['coordinate'][1])))
            self.tableWidget_stars.setItem(i, 3, QTableWidgetItem(str(star['GP'])))
        self.tableWidget_stars.resizeColumnsToContents()

        # 计算像素焦距
        if len(self.data.stars) >= 2:
            z = self.data.get_z()
            self.label_z.setText(str(z))
        else:
            self.label_z.setText('-')
            self.data.z = None

        self.check()

    def add_star(self):
        """添加/修改星星"""
        # 弹出子窗口
        self.w = QDialog()
        ui = Ui_DialogAddStar()
        ui.setupUi(self.w)
        if self.w.exec():
            # 获取子窗口数据
            name = ui.lineEdit_name.text()
            x = float(ui.lineEdit_x.text())
            y = float(ui.lineEdit_y.text())
            hour_angle = ui.lineEdit_hour_angle.text()
            declination = ui.lineEdit_declination.text()
            # 写入数据
            self.data.add_star(name, x, y, hour_angle, declination)
            # 更新表格
            self.update_table()

    def del_star(self):
        """删除星星"""
        selected = self.tableWidget_stars.selectedItems()
        rows = list(set([i.row() for i in selected]))
        for row in rows:
            name = self.tableWidget_stars.item(row, 0).text()
            del self.data.stars[name]
        self.update_table()

    def import_stars(self):
        """导入星星"""
        path = QFileDialog.getOpenFileName(self, '导入星星', None, '文本文件 (*.txt);;Python序列化文件 (*.pickle)')[0]
        if path:
            if path.endswith('.txt'):
                with open(path, 'r', encoding='utf-8') as f:
                    for line in f:
                        name, x, y, hour_angle, declination = line.split()
                        self.data.add_star(name, float(x), float(y), hour_angle, declination)
            elif path.endswith('.pickle'):
                with open(path, 'rb') as f:
                    self.data.stars = pickle.load(f)
            self.update_table()

    def export_stars(self):
        """导出星星"""
        path = QFileDialog.getSaveFileName(self, '导出星星', None, 'Python序列化文件 (*.pickle)')[0]
        if path:
            with open(path, 'wb') as f:
                pickle.dump(self.data.stars, f)

    def browse(self):
        """浏览标注直线的文件并计算天顶坐标"""
        path = QFileDialog.getOpenFileName(self, '标注了指向天顶的直线的图片', None, '图片 (*.jpg *.png)')[0]
        if path:
            self.lineEdit_lines_path.setText(path)
            if self.radioButton_r.isChecked():
                colour = 'red'
            elif self.radioButton_g.isChecked():
                colour = 'green'
            else:
                colour = 'blue'
            zenith = get_zenith(path, colour)
            self.data.zenith = zenith
            self.label_zenith.setText(str(zenith))

            self.check()

    def check(self):
        """检查定位计算是否就绪"""
        self.pushButton_calc.setEnabled(self.data.z is not None and self.data.zenith is not None)

    def calc(self):
        """定！位！计！算！"""
        lat_lon, address = calc(self.data)
        self.label_lat_lon.setText(lat_lon)
        self.label_address.setText(address)
