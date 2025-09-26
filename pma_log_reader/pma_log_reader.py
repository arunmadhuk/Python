"""
A Python Script to read PMA logs and analyse the power on & Shutdown WorkFlow
"""

import os
import json
from export_style import *
import datetime
import os.path as p
import pandas as pd


pma_log_folder = "Auto-PMA"
pma_script_version = "Automation script version 1.0.6000"
last_show = "Last show is finished"
perform_shutdown = "performing shutdown workflow ..."
end_shutdown = "ending shutdown workflow ..."
transfer_finished_check = "no on going or pending transfer found"


def get_log_files(log_path):
    """
    returns the .log files from the given pma script log path
    :param log_path:
    :return:log_files
    """
    log_files = []
    for log_file in os.listdir(log_path):
        if log_file.endswith(".log"):
            log_files.append(log_file.split('.log')[0])

    return log_files


def generate_excel_report(excel_prefix_name, pma_log_dict):
    print(json.dumps(pma_log_dict, indent=4))

    current_date = datetime.datetime.now()

    date = str(current_date.day).zfill(2) + str(current_date.month).zfill(2) + str(current_date.year)
    time = "{}{}{}".format(str(current_date.hour), str(current_date.minute), str(current_date.second))
    export_time = "{}_{}".format(date, time)
    export_file_name = excel_prefix_name + "_" + export_time + ".xls"

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('PMA Log Summary')  # this will make a sheet named PMA Log Summary

    # Sheet header, first row
    row_num = 0

    # Header Column
    columns = ['Date', 'Screen Name', 'Power On Script Executed on', 'Shutdown Script Executed on',
               'Last Show Ended logged at', 'Shutdown Workflow Performed on', 'Shutdown Script Next executed on']

    for col_num in range(len(columns)):
        ws.col(col_num).width = col_width
        ws.write(row_num, col_num, columns[col_num], style_head_row)  # at 0 row 0 column

    print("Excel Export file Name : '{}'".format(export_file_name))
    wb.save(export_file_name)


def check_power_on_script_started_timing(log_file):
    logs = open(log_file, 'r')
    power_on_timing = []
    for log in logs:
        if pma_script_version in log:
            split = log.split(pma_script_version)
            power_on_timing.append(split[0])
    return power_on_timing


def check_power_on_script_log_files(log_path, log_files):
    """
    checks the power on script for power on timing
    :param log_path:
    :param log_files:
    :return:power_on_dict
    """
    power_on_dict = {}
    for logfile in log_files:
        script_date = logfile
        logfile = logfile+".log"
        power_on_timing = check_power_on_script_started_timing(os.path.join(log_path, logfile))
        power_on_dict[script_date] = power_on_timing
    return power_on_dict


def check_shutdown_script_log_files(log_path, log_files):
    """
    Checks the shutdown script log files for script started timing, last show finished shutdown workflow
    """
    shutdown_script_dict = {}
    script_run_dict = {}
    last_show_dict = {}
    perform_shutdown_dict = {}
    transfer_finished_check_dict = {}

    for logfile in log_files:
        script_date = logfile
        logfile = logfile + ".log"
        shutdown_log = os.path.join(log_path, logfile)
        logs = open(shutdown_log, 'r')
        script_run_timing = []
        last_show_timings = []
        perform_shutdown_timing = []
        transfer_finished_timing = []

        for log in logs:
            if pma_script_version in log:
                split = log.split(pma_script_version)
                script_run_timing.append(split[0])
            elif last_show in log:
                split = log.split(last_show)
                last_show_timings.append(split[0])
            elif perform_shutdown in log:
                split = log.split(perform_shutdown)
                perform_shutdown_timing.append(split[0])
            elif transfer_finished_check in log:
                split = log.split(transfer_finished_check)
                transfer_finished_timing.append(split[0])

        script_run_dict[script_date] = script_run_timing
        last_show_dict[script_date] = last_show_timings
        perform_shutdown_dict[script_date] = perform_shutdown_timing
        transfer_finished_check_dict[script_date] = transfer_finished_timing

    shutdown_script_dict["script_run"] = script_run_dict
    shutdown_script_dict["last_show_finished"] = last_show_dict
    shutdown_script_dict["perform_shutdown"] = perform_shutdown_dict
    shutdown_script_dict["transfer_finished"] = transfer_finished_check_dict
    # print(shutdown_script_dict)
    return shutdown_script_dict


def create_pma_log_dict_screenwise(pma_log_path):
    """
    Gets the screen names from the Auto_PMA folder.
    param pma_log_path:
    :return:screen_names
    """
    pma_log_folders = next(os.walk(pma_log_path))[1]
    screen_names = {}

    for log_folder in pma_log_folders:

        if log_folder.__contains__("-power-on"):
            split = "-power-on"
        elif log_folder.__contains__("-shutdown"):
            split = "-shutdown"

        screen_name = log_folder.split(split)[0]

        if screen_name not in screen_names.keys():
            screen_names[screen_name] = {}

        script_log_path = os.path.join(pma_log_path, log_folder)
        script_log_files = get_log_files(script_log_path)
        screen_names[screen_name][log_folder] = script_log_files
        # print(script_log_files)

    return screen_names


def check_auto_pma_log_present(log_path):
    """
    Checkes whether the given TMS log path has "Auto-PMA" logs
    :param log_path:
    :return:
    """
    child_directories = next(os.walk(log_path))[1]
    if pma_log_folder in child_directories:
        print("The given TMS log path : '{}' is valid".format(log_path))
        child_path = os.path.join(log_path, pma_log_folder)

        pma_log_path = os.path.join(log_path, pma_log_folder)
        print(pma_log_path)
        pma_log_dict = create_pma_log_dict_screenwise(pma_log_path)
        screen_names = list(pma_log_dict.keys())
        # print("screen_names : '{}'".format(screen_names))
        common_prefix = p.commonprefix(screen_names)
        site_name = common_prefix.split("-Hall")[0]
        print("Site name : '{}'".format(site_name))
        log_date_range = set()
        for screen_name in screen_names:
            script_files = pma_log_dict[screen_name].keys()
            for script_file in script_files:

                script_log_files = pma_log_dict[screen_name][script_file]
                # print("log_files : {}".format(script_log_files))
                for date in script_log_files:
                    log_date_range.add(datetime.datetime.strptime(date, '%Y-%m-%d').date())

                script_file_log_path = os.path.join(pma_log_path, script_file)
                if "power-on" in script_file:
                    power_on_log_dict = check_power_on_script_log_files(script_file_log_path, script_log_files)
                    pma_log_dict[screen_name][script_file] = power_on_log_dict
                if "shutdown" in script_file:
                    shutdown_log_dict = check_shutdown_script_log_files(script_file_log_path, script_log_files)
                    pma_log_dict[screen_name][script_file] = shutdown_log_dict

        sorted_log_dates = sorted(log_date_range)
        start_date = sorted_log_dates[0].strftime("%d-%m-%Y")
        end_date = sorted_log_dates[-1].strftime("%d-%m-%Y")
        print("log date start  : '{}',  end : '{}'".format(start_date, end_date))
        excel_prefix_name = site_name+"_"+start_date + " to "+end_date
        generate_excel_report(excel_prefix_name, pma_log_dict)

    else:
        print("The given TMS log path : '{}' is invalid".format(log_path))


tms_log_path = ".\\TmsLogsExport_20221005114630"
check_auto_pma_log_present(tms_log_path)
