import os
import sys
from datetime import datetime

from PyQt5.QtWidgets import *

from tms_log_reader_ui import LogReaderUI


class TMSLogReader:
    log_dates = []

    def initialize_log_reader(self):
        year = datetime.now().year
        log_file_path = "D:\\Python\\tms_log\\TmsLogsExport_20220426013813"

        # log_file_path = "D:/Logs/Malaysia/Dadi Cinema/Dadi Pavilion 15-04-22/TmsLogsExport_20220415104013"
        gdc_tms_log_folder = "GDC TMS\\log\\{}".format(year)
        gdc_tms_user_log_folder = "GDC TMS\\UserLogs\\{}".format(year)
        gdc_tms_log_path = os.path.join(log_file_path, gdc_tms_log_folder)
        print("gdc_tms_log_folder {}".format(gdc_tms_log_path))
        log_files, self.log_dates = self.get_log_files(gdc_tms_log_path)
        # self.set_log_range(self.log_dates)

        print("log_files  {} ".format(log_files))

        gdc_tms_user_log_path = os.path.join(log_file_path, gdc_tms_user_log_folder)
        print("gdc_tms_user_log_folder {}".format(gdc_tms_user_log_path))
        usr_log_files, usr_log_dates = self.get_log_files(gdc_tms_user_log_path)

        print("usr_log_files  {} ".format(usr_log_files))
        print("usr_log_files start date -- {}".format(usr_log_dates[0]))
        print("usr_log_files End date -- {}".format(usr_log_dates[-1]))

    def get_log_files(self, log_path):
        dates = []
        if os.path.exists(log_path):
            logs = os.listdir(log_path)
            for log_file in logs:
                log_date = log_file.split(".log")[0]
                dates.append(log_date)
                # log_datetime= datetime.strptime(log_date,"%Y-%m-%d")
                # print("log_datetime --- {}".format(log_datetime))
                # print("log_datetime month --- {}".format(log_datetime.month))
        else:
            raise Exception("The path {} doesn't exists".format(log_path))

        return logs, dates


if __name__ == '__main__':
    app = QApplication([])
    log_reader_ui = LogReaderUI()
    log_reader = TMSLogReader()

    log_reader.initialize_log_reader()
    print(log_reader.log_dates)
    log_reader_ui.show()
    log_reader_ui.set_start_and_end_date(log_reader.log_dates)

    app.exec_()
