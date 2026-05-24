# Auto-forward Windows localhost:8080 to WSL2
$WslIp = wsl bash -c "hostname -I" 2>$null
if ($WslIp) {
    $WslIp = $WslIp.Trim().Split(" ")[0]
    netsh interface portproxy delete v4tov4 listenport=8080 listenaddress=0.0.0.0 2>$null
    netsh interface portproxy add v4tov4 listenport=8080 listenaddress=0.0.0.0 connectport=8080 connectaddress=$WslIp
    Write-Host "Port 8080 forwarded to $WslIp"
}
