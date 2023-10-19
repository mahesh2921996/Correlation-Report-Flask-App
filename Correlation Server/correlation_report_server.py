# Import necessary libraries
from flask import Flask, render_template, request
# from gevent.pywsgi import WSGIServer
from gevent import pywsgi

import pandas as pd
from config.Config import Info_Server
from util.helper import Helper
import re

# Import user-defined library
from scripts.correlation_report import Correlation_report

# Initialize flask server.
app = Flask(__name__)

# Initialize the Helper object.
help_obj = Helper()

# Initialize the global object.
global global_corr_obj


@app.route("/")
def show_table():
    """This method is used to show the upload setup to user."""
    return render_template("report.html", name="", table_col=[], table_data=[])

@app.route('/load_data', methods=['POST'])
def report():
    """This method is used to help the load data from file."""
    table_data = []
    table_col = []
    error_message = ""
    if request.method == 'POST':
        f = request.files['file']

        if str(f).find("(") > 17:
            file_flag_1 = re.findall("text/csv", str(f))
            file_flag_2 = re.findall("xlsx", str(f))

            if len(file_flag_1) or len(file_flag_2) > 0:

                if len(str(f)) != 0:
                    try:
                        if len(file_flag_1)>0:
                            df = pd.read_csv(f)
                        else:
                            df = pd.read_excel(f)

                        if len(df) != 0:
                            corr_obj = Correlation_report(df)

                            global global_corr_obj
                            global_corr_obj = corr_obj

                    except Exception as err:
                        print(err)
            else:
                error_message = "Please choose only proper csv or excel file to upload."
                return render_template("report.html", error=error_message)
        else:
            error_message = "Please choose any csv or excel file to upload."
            return render_template("report.html", error=error_message)
        return render_template("report.html", name="", table_col=table_col, table_data=table_data, error=error_message, custom_block = False, drop_block=True)

@app.route("/show_very_strong_result")
def show_very_strong_result():
    """The user can see the data frame's very strong correlation columns by using this method."""
    global global_corr_obj
    global_corr_df = global_corr_obj.very_strong_corr()

    table_data, table_col = help_obj.make_table_data(global_corr_df)

    # Render the HTML template with the table data
    return render_template("report.html", name="Very Strong Correlation Report", table_col=table_col, table_data=table_data, custom_block = False, drop_block=True)

@app.route("/show_strong_result")
def show_strong_result():
    """The user can see the data frame's strong correlation columns by using this method."""
    try:
        global global_corr_obj
        global_corr_df = global_corr_obj.strong_corr()

        table_data, table_col = help_obj.make_table_data(global_corr_df)

        # Render the HTML template with the table data
        return render_template("report.html", name="Strong Correlation Report", table_col=table_col, table_data=table_data, custom_block = False, drop_block=True)
    except Exception as err:
        print(err)


@app.route("/show_moderate_result")
def show_moderate_result():
    """The user can see the data frame's moderate correlation columns by using this method."""
    global global_corr_obj
    global_corr_df = global_corr_obj.moderate_corr()

    table_data, table_col = help_obj.make_table_data(global_corr_df)

    # Render the HTML template with the table data
    return render_template("report.html", name="Moderate Correlation Report", table_col=table_col, table_data=table_data, custom_block = False, drop_block=True)


@app.route("/show_weak_result")
def show_weak_result():
    """The user can see the data frame's weak correlation columns by using this method."""
    global global_corr_obj
    global_corr_df = global_corr_obj.weak_corr()

    table_data, table_col = help_obj.make_table_data(global_corr_df)

    # Render the HTML template with the table data
    return render_template("report.html", name="Weak Correlation Report", table_col=table_col, table_data=table_data, custom_block = False, drop_block=True)

@app.route("/show_very_weak_result")
def show_very_weak_result():
    """The user can see the data frame's very weak correlation columns by using this method."""
    global global_corr_obj
    global_corr_df = global_corr_obj.very_weak_corr()

    table_data, table_col = help_obj.make_table_data(global_corr_df)

    # Render the HTML template with the table data
    return render_template("report.html", name="Very Weak Correlation Report", table_col=table_col, table_data=table_data, custom_block = False, drop_block=True)

@app.route("/show_no_corr_result")
def show_no_corr_result():
    """The user can see the data frame's no correlation columns by using this method."""
    global global_corr_obj
    global_corr_df = global_corr_obj.no_corr()

    table_data, table_col = help_obj.make_table_data(global_corr_df)

    # Render the HTML template with the table data
    return render_template("report.html", name="No Correlation Report", table_col=table_col, table_data=table_data, custom_block = False, drop_block=True)

@app.route("/show_customize_result", methods=["POST", "GET"])
def show_customize_result():
    """The user can see the data frame's customize correlation columns by using this method."""
    table_col = []
    table_data = []
    if request.method == "POST":

        s_lrange = request.form.get("lori")
        s_urange = request.form.get("uori")

        slider_lrange = float(s_lrange)
        slider_urange = float(s_urange)

        if slider_lrange == slider_urange:
            error = "Please don't choose same value!"
            return render_template("report.html", error=error, drop_block=True)

        else:
            if slider_lrange < slider_urange:
                sl = slider_lrange
                su = slider_urange
            elif slider_urange < slider_lrange:
                sl = slider_urange
                su = slider_lrange

            global global_corr_obj
            global_corr_df = global_corr_obj.customize_corr(sl, su)

            table_data, table_col = help_obj.make_table_data(global_corr_df)

            return render_template("report.html", name="Custom Correlation Report", table_col=table_col, table_data=table_data, custom_block = False, lrange=sl, hrange=su, drop_block=True)

    return render_template("report.html", name="", table_col=table_col, table_data=table_data, custom_block = True, drop_block=True)

@app.route("/help")
def help():
    """This method is used to show help page to user."""
    table_col = ["Correlation Types", "Ranges"]
    table_data = [["Very Strong Correlation", "+/- 0.95 to +/- 1"], ["Strong Correlation", "+/- 0.70 to +/- 0.95"], ["Moderate Correlation", "+/- 0.50 to +/- 0.70"], ["Weak Correlation", "+/- 0.25 to +/- 0.50"], ["Very Weak Correlation", "+0.25 to -0.25"], ["No Correlation", "0"], ["Custom Correlation", "Choose both the higher and lower ranges between -1 and +1."]]
    return render_template("help.html", table_col=table_col, table_data=table_data)

if __name__ == '__main__':
    # app.run(host="172.16.110.31", port=8045)
    # app.run(host=Info_Server.HOST.value, port=Info_Server.PORT.value)
    print("Server started!")

    # http_server = WSGIServer((Info_Server.HOST.value, Info_Server.PORT.value), app)
    http_server = pywsgi.WSGIServer(('0.0.0.0', 443), app, keyfile='security/server.key', certfile='security/server.crt')
    http_server.serve_forever()


    # http://127.0.0.1:8045/
    # https://172.16.110.31:443/
