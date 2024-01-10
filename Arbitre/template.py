#!/usr/bin/env python
# coding:utf-8

def write_template(port, file_dest):
    template_string = """<!DOCTYPE html>
    <html lang="en">

    <head>
    	<title>Hey !!</title>
    	<meta charset="UTF-8">
    	<meta name="viewport" content="width=device-width, initial-scale=1">
    	<link rel="shortcut icon" href="{{{{ url_for('static', filename='img/avatar.png') }}}}" />
    	<link rel="stylesheet" href="{{{{ url_for('static', filename='w3c/css/w3.css') }}}}">
    	<link rel="stylesheet" href="{{{{ url_for('static', filename='fonts/font-awesome-4.7.0/css/font-awesome.min.css') }}}}">
    	<link rel="stylesheet" href="{{{{ url_for('static', filename='bootstrap/css/bootstrap.min.css') }}}}">
        <link rel="stylesheet" href="{{{{ url_for('static', filename='highlight/default.min.css')}}}}">
    	<style>
    		td {{
    			font-size: smaller;
    		}}
            .debug-toolbar {{
                position: fixed;
                top: 60px;
                right: 20px;
                z-index: 9999;
            }}
            .debug-toolbar-toggle {{
                display: inline-block;
                padding: 8px 12px;
                background-color: #6c757d;
                color: #fff;
                text-decoration: none;
                font-size: 14px;
                line-height: 1;
                border-radius: 4px;
                cursor: pointer;
            }}
            .debug-toolbar-panel {{
                display: none;
                position: fixed;
                top: 100px;
                right: 20px;
                width: 100px;
                max-height: 400px;
                overflow-y: auto;
                background-color: #f8f9fa;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3);
                padding: 10px;
                font-size: 12px;
                line-height: 1.5;
                z-index: 9999;
            }}
            .debug-toolbar-toggle.open {{
            }}
            .debug-toolbar-toggle.open:hover {{
            }}
            .debug-toolbar-toggle.open + .debug-toolbar-panel {{
                display: block;
            }} 
    	</style>
    	<script src="{{{{ url_for('static', filename='js/jquery.min.js') }}}}"></script>
    	<script src="{{{{ url_for('static', filename='js/popper.min.js') }}}}"></script>
    	<script src="{{{{ url_for('static', filename='bootstrap/js/bootstrap.min.js') }}}}"></script>
    	<script src="{{{{ url_for('static', filename='highlight/highlight.min.js') }}}}"></script>
    	<script src="{{{{ url_for('static', filename='vega/vega@5.20.2') }}}}"></script>
    	<script src="{{{{ url_for('static', filename='vega/vega-lite@5.3.0') }}}}"></script>
    	<script src="{{{{ url_for('static', filename='vega/vega-embed@6.18.2') }}}}"></script>
    	<script src="{{{{ url_for('static', filename='vega/vega-embed@6.18.2') }}}}"></script>
    	<!--script src="https://cdn.jsdelivr.net/npm/vega@5.20.2"></script>
    	<script src="https://cdn.jsdelivr.net/npm/vega-lite@5.3.0"></script>
    	<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.18.2"></script-->

    </head>

    <body>
        <div class="container text-center">

        <!-- floating left menu debug-toolbar like... -->
        <div class="debug-toolbar">
            <a href="#" class="btn btn-primary debug-toolbar-toggle">Toolbar</a>
            <div class="debug-toolbar-panel">
                <!-- Debug toolbar content goes here -->
                <div class="row">
                    <div class="container-fluid">
                        <div class="row"> 
                            <div class="col-sm-6">
                                <div class="btn-group-vertical">
                                    <button type="button" class="btn btn-danger" id="Stop">Stop</button>
                                    <button type="button" class="btn btn-primary" id="BrokersBtn">Brokers</button>
                                    <button type="button" class="btn btn-primary" id="TickersBtn">Tickers</button>
                                    <button type="button" class="btn btn-primary" id="AlgoBtn">Algo</button>
                                    <button type="button" class="btn btn-info" data-toggle="collapse" data-target="#LiveDatas">Datas</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        </div>

            <br>        <br>
            <div class="row">
                <div class="col-sm-6">
                    <h1>Ask</h1>
    				<div id="ask"></div>
                </div>
                <div class="col-sm-6">
                    <h1>Bid</h1>
    				<div id="bid"></div>
                </div>
            </div>


            <br>
            <br>

            <!-- Modal -->
            <div class="modal fade" id="Tickers" role="dialog">
                <div class="modal-dialog modal-sm">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h4 class="modal-title">Tickers</h4>
                            <button type="button" class="close" data-dismiss="modal">&times;</button>
                        </div>

                        <div class="modal-body">
                            <div class="table-responsive">
                                <table class="table table-striped table-bordered table-condensed">
                                    <tbody id="TickersBody">
                                        <!-- Data will be inserted here -->
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Modal -->
            <div class="modal fade" id="Brokers" role="dialog">
                <div class="modal-dialog modal-sm">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h4 class="modal-title">Brokers</h4>
                            <button type="button" class="close" data-dismiss="modal">&times;</button>
                        </div>

                            <div class="modal-body">
                                <div class="table-responsive">
                                    <table class="table table-striped table-bordered table-condensed">
                                        <tbody id="BrokersBody">
                                            <!-- Data will be inserted here -->
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                    </div>
                </div>
              </div>

            <!-- Modal -->
            <div class="modal fade" id="Algo" role="dialog">
                <div class="modal-dialog modal-lg">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h4 class="modal-title">Algo</h4>
                            <button type="button" class="close" data-dismiss="modal">&times;</button>
                        </div>

                            <div class="modal-body">
                                <div class="table-wrapper">
                                    <div class="table-responsive">
                                        <table class="table table-striped table-bordered table-condensed">
                                            <pre><code class="python" id="AlgoBody">
                                                <tbody id="AlgoBody">
                                                <!-- Data will be inserted here -->
                                                </tbody>
                                            </code></pre>
                                        </table>
                                    </div>
                                </div>
                            </div>

                    </div>
                </div>
              </div>

            <div class="row">
                <div id="LiveDatas" class="collapse">
                    <div class="col-sm-12">
                        <div class="card">
                            <div class="card-body">
                                <h1>Datas</h1>
                                <div class="table-responsive">
                                    <table class="table table-striped table-bordered table-condensed ">
                                        <tbody id="datas">
                                            <!-- Data will be inserted here -->
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>


            <script>
                hljs.initHighlightingOnLoad();
                $(document).ready(function () {{

                    $('.debug-toolbar-toggle').click(function(e) {{
                        e.preventDefault();
                        $(this).toggleClass('open');
                        $('.debug-toolbar-panel').toggle();
                    }});

                    $("#Stop").click(function(){{
                        postExec('http://127.0.0.1:{0}/json_stop_arbitre');
                    }});

                    $("#BrokersBtn").click(function(){{
                        getJsonData('http://127.0.0.1:{0}/json_brokers', "#BrokersBody", dictOneEntryToTable);
                        $("#Brokers").modal();
                    }});

                    $("#TickersBtn").click(function(){{
                        getJsonData('http://127.0.0.1:{0}/json_tickers', "#TickersBody", dictOneEntryToTable);
                        $("#Tickers").modal();
                    }});

                    $("#AlgoBtn").click(function(){{
                        getPlainTextData('http://127.0.0.1:{0}/json_algo', "#AlgoBody", putPlainTextInElement);
                        $("#Algo").modal();
                    }});

                    function putPlainTextInElement(data, elementId) {{
                        const tableContainer = $(elementId);
                        tableContainer.empty(); // Clear existing content
                        if (!data) {{
                            tableContainer.html('<p>No data available</p>');
                            return;
                        }}
                        tableContainer.html(data)
                        hljs.highlightBlock(tableContainer)
                    }}

                    function getPlainTextData(endpoint, elementId, funcPtr) {{
                        $.ajax({{
                            url: endpoint,
                            method: 'GET',
                            dataType: 'text',
                            success: function(data) {{
                                funcPtr(data, elementId);
                            }}
                        }});
                    }}

                    function getJsonData(endpoint, elementId, funcPtr){{
                        $.ajax({{
                            url: endpoint,
                            method: 'GET',
                            dataType: 'json',
                            success: function(data) {{
                                funcPtr(data, elementId);
                            }}
                        }});
                    }}

                    function postExec(endpoint){{
                        $.ajax({{
                            url: endpoint,
                            method: 'POST',
                            dataType: 'json',
                        }});
                    }}

                    function dictOneEntryToTable(data, elementId) {{
                        const tableContainer = $(elementId);
                        tableContainer.empty(); // Clear existing content
                        if (!data || Object.keys(data).length === 0) {{
                            tableContainer.html('<p>No data available</p>');
                            return;
                        }}
                        // headers
                        const table = $('<table>').addClass('table table-bordered table-hover');
                        const tableHeader = $('<thead>');
                        const headerRow = $('<tr>');
                        const header = Object.keys(data)[0]; // Get the dictionary key
                        headerRow.append($('<th>').text(header));
                        tableHeader.append(headerRow);
                        table.append(tableHeader);
                        // body
                        const tableBody = $('<tbody>');
                        const items = data[header]; // Get the list of items
                        items.forEach(item => {{
                            const row = $('<tr>');
                            const cell = $('<td>').text(item);
                            row.append(cell);
                            tableBody.append(row);
                        }});
                        table.append(tableBody);
                        // complete table
                        tableContainer.append(table);
                    }}

                    function tupleHeaderedTotable(data, elementId) {{
                        const tableContainer = $(elementId);
                        tableContainer.empty(); // Clear existing content
                        if (!data || data.length === 0) {{
                          tableContainer.html('<p>No data available</p>');
                          return;
                        }}
                        // Extract headers
                        const headers = data[0];
                        const rows = data.slice(1);
                        // headers
                        const table = $('<table>').addClass('table table-bordered table-hover');
                        const tableHeader = $('<thead>');
                        const headerRow = $('<tr>');
                        headers.forEach(header => {{
                          const headerCell = $('<th>').text(header);
                          headerRow.append(headerCell);
                        }});
                        tableHeader.append(headerRow);
                        table.append(tableHeader);
                        // body
                        const tableBody = $('<tbody>');
                        rows.forEach(row => {{
                          const dataRow = $('<tr>');
                          row.forEach(cellData => {{
                            const cell = $('<td>').text(cellData);
                            dataRow.append(cell);
                          }});
                          tableBody.append(dataRow);
                        }});
                        table.append(tableBody);
                        // complete table
                        tableContainer.append(table);
                    }}

                    function dictionaryTotable(data, elementId) {{
                        const tableContainer = $(elementId);
                        tableContainer.empty(); // Clear existing content
                        if (!data || Object.keys(data).length === 0) {{
                          tableContainer.html('<p>No data available</p>');
                          return;
                        }}
                        // Extract headers and values
                        const headers = Object.keys(data);
                        const values = Object.values(data);
                        // headers
                        const table = $('<table>').addClass('table table-bordered table-hover');
                        const tableHeader = $('<thead>');
                        const headerRow = $('<tr>');
                        headers.forEach(header => {{
                          const headerCell = $('<th>').text(header);
                          headerRow.append(headerCell);
                        }});
                        tableHeader.append(headerRow);
                        table.append(tableHeader);
                        // body
                        const tableBody = $('<tbody>');
                        const dataRow = $('<tr>');
                        values.forEach(value => {{
                          const cell = $('<td>').text(value);
                          dataRow.append(cell);
                        }});
                        tableBody.append(dataRow);
                        table.append(tableBody);
                        // complete table
                        tableContainer.append(table);
                    }}

                    function refreshData() {{
                        $.ajax({{
                            url: 'http://127.0.0.1:{0}/json_data',
                            dataType: 'json',
                            success: function (data) {{
                                const headers = data['data'][0];
                                let table = '<table class="table table-striped table-bordered table-hover"><thead><tr>';
                                for (let i = 0; i < headers.length; i++) {{
                                    table += '<th>' + headers[i] + '</th>';
                                }}
                                table += '</tr></thead><tbody>';
                                for (let i = 1; i < data['data'].length; i++) {{
                                    table += '<tr>';
                                    for (let j = 0; j < headers.length; j++) {{
                                        table += '<td>' + data['data'][i][j] + '</td>';
                                    }}
                                    table += '</tr>';
                                }}
                                table += '</tbody></table>';
                                $('#datas').html(table);

                                function transformData(inputData) {{
                                    // Parse the input data as JSON
                                    const dataObj = JSON.parse(inputData);
                                    // Extract the headers from the first element of the 'data' array
                                    const headers = dataObj['data'][0];
                                    // Extract the list of data rows (excluding the headers)
                                    const dataList = dataObj['data'].slice(1);

                                    // Map each data row to an object with the expected property names
                                    const transformedData = dataList.map(dataRow => {{
                                        const dataObj = {{}};
                                        for (let i = 0; i < headers.length; i++) {{
                                            const header = headers[i];
                                            const value = dataRow[i];
                                            dataObj[header] = value;
                                        }}
                                        return dataObj;
                                    }});

                                    return transformedData;
                                }}

                                function updateChart(data) {{
                                    ask.data.values = data;
                                    vegaEmbed('#ask', ask);
                                    bid.data.values = data;
                                    vegaEmbed('#bid', bid);
                                }}

                                const ask = {{
                                    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
                                    //"$schema": "./static/vega/v5.json",
                                    //"$schema": "{{{{ url_for('static', filename='vega/v5.json') }}}}",
                                    "data": {{
                                        "values": ""
                                    }},
                                    "width": 500,
                                      "height": 500,
                                      "autosize": {{"type": "fit-x"}},
                                    "mark": {{ "type": "line", "point": true }},
                                    "encoding": {{
                                        "color": {{ "field": "broker", "type": "nominal" }},
                                        "x": {{ "field": "time", "type": "temporal" }},
                                        "y": {{
                                            "field": "ask",
                                            "type": "quantitative",
                                            "scale": {{ "zero": false, "nice": true }}
                                        }},
                                    }}
                                }};

                                const bid = {{
                                    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
                                    //"$schema": "./static/vega/v5.json",
                                    //"$schema": "{{{{ url_for('static', filename='vega/v5.json') }}}}",
                                    "data": {{
                                        "values": ""
                                    }},
                                    "width": 500,
                                      "height": 500,
                                      "autosize": {{"type": "fit-x"}},
                                    "mark": {{ "type": "line", "point": true }},
                                    "encoding": {{
                                        "color": {{ "field": "broker", "type": "nominal" }},
                                        "x": {{ "field": "time", "type": "temporal" }},
                                        "y": {{
                                            "field": "bid",
                                            "type": "quantitative",
                                            "scale": {{ "zero": false, "nice": true }}
                                        }},
                                    }}
                                }};

                                const transformedData = transformData(JSON.stringify(data));
                                updateChart(transformedData);
                            }}
                        }});
                    }}

                    refreshData();
                    setInterval(refreshData, 1000); // Refresh every 1 second
                }});
            </script>
    </body>

    </html>""".format(port)

    with open(file_dest, "w") as template_file:
        template_file.write(template_string)

