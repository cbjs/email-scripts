<html>
<head>
  <title>email html title</title>
</head>
<style type="text/css">
div#log-pagewrap
{
	font-family: "Lucida Sans Unicode", "Lucida Grande", Sans-Serif;
	font-size: 13px;
	width: 800px;
	margin: 0 auto;
}
div#log-pagewrap h2 {
  font-size: 1.2em;
  font-weight: bold;
  text-align: center;
}
div#log-pagewrap table 
{
  width: 100%;
  font-size: 1em;
	text-align: left;
	border-collapse: collapse;
	border: 1px solid #69c;
}
div#log-pagewrap table caption
{
  text-align: right;
}
div#log-pagewrap table th
{
	padding: 12px 17px 12px 17px;
	font-weight: normal;
	font-size: 1.15em;
	color: #039;
	border-bottom: 1px dashed #69c;
}
div#log-pagewrap table td
{
	padding: 7px 17px 7px 17px;
	color: #669;
}
div#log-pagewrap table tbody tr:hover td
{
	color: #339;
	background: #d0dafd;
}
div#log-pagewrap table tbody tr.even-row 
{
	color: #339;
	background: #d0dafd;
}
</style>
<body>
<div id="log-pagewrap">
  <h2>log analysis</h2>
  <table>
    <thead>
      <th>host</th>
      <th>total</th>
      <th>success</th>
      <th>fail</th>
      <th>lost</th>
      <th>exist</th>
    </thead>
    <tbody>
    {% for item in result %}
    <tr class="{{ 'odd-row' if loop.index % 2 else 'even-row' }}">
      <td>{{ item }}</td>
      <td>{{ result[item]['total'] }}</td>
      <td>{{ result[item]['success'] }}</td>
      <td>{{ result[item]['fail'] }}</td>
      <td>{{ result[item]['apk_lost'] }}</td>
      <td>{{ result[item]['apk_exist'] }}</td>
    {% endfor %}
    </tr>
    </tbody>
  </table>
</div>
</body>
</html>
