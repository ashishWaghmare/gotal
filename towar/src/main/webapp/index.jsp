<html>
<body>
<h2>Hello World!</h2>
<p>
It is now
<%= new java.util.Date() %></p>
<p>
You are coming from 
<%= request.getRemoteAddr()  %></p>
<p>
Server host name is
<b><%=request.getServerName() %></b></p>
</body>
</html>
