def generate_data(report_file):
    ''' SOME YOUR CODE '''
    report_file.write("<p>Put some code hiere</p>")

def generate_template():
    with open("report.html", 'w+') as report_file:
        report_file.write('<html>\n<head>\n<style>body{font: 1.5em;},table {font-family: arial, sans-serif;border-collapse: collapse;width: 100%;}td, th {border: 1px solid #dddddd;text-align: left;padding: 8px;}tr:nth-child(even) {background-color: #dddddd;}</style></head><body>\n<center>\n<h1>Report</h1>\n')

        generate_data(report_file)

        report_file.write("</body></html>")

def main():
    generate_template()

if __name__ == "__main__":
    main()
