import subprocess;
import sys;
import pyautogui;
import datetime;

#Base64 encoded "../scripts/screenshot.ps1"
scriptPs = "VAByAHkACgB7AAoAJABfAGQAYQB0AGUAPQAgACgARwBlAHQALQBEAGEAdABlACkALgB0AG8AcwB0AHIAaQBuAGcAKAAiAGQAZAAtAE0ATQAtAHkAeQB5AHkAfgBIAEgALQBtAG0ALQBzAHMAIgApAAoAJABGAGkAbABlAE4AYQBtAGUAIAA9ACAAIgAkACgAJABfAGQAYQB0AGUAKQAuAHAAbgBnACIACgBBAGQAZAAtAFQAeQBwAGUAIAAtAEEAcwBzAGUAbQBiAGwAeQBOAGEAbQBlACAAUwB5AHMAdABlAG0ALgBXAGkAbgBkAG8AdwBzAC4ARgBvAHIAbQBzAAoAQQBkAGQALQB0AHkAcABlACAALQBBAHMAcwBlAG0AYgBsAHkATgBhAG0AZQAgAFMAeQBzAHQAZQBtAC4ARAByAGEAdwBpAG4AZwAKACMAIABHAGEAdABoAGUAcgAgAFMAYwByAGUAZQBuACAAcgBlAHMAbwBsAHUAdABpAG8AbgAgAGkAbgBmAG8AcgBtAGEAdABpAG8AbgAKACQAUwBjAHIAZQBlAG4AIAA9ACAAWwBTAHkAcwB0AGUAbQAuAFcAaQBuAGQAbwB3AHMALgBGAG8AcgBtAHMALgBTAHkAcwB0AGUAbQBJAG4AZgBvAHIAbQBhAHQAaQBvAG4AXQA6ADoAVgBpAHIAdAB1AGEAbABTAGMAcgBlAGUAbgAKACQAVwBpAGQAdABoACAAPQAgACQAUwBjAHIAZQBlAG4ALgBXAGkAZAB0AGgACgAkAEgAZQBpAGcAaAB0ACAAPQAgACQAUwBjAHIAZQBlAG4ALgBIAGUAaQBnAGgAdAAKACQATABlAGYAdAAgAD0AIAAkAFMAYwByAGUAZQBuAC4ATABlAGYAdAAKACQAVABvAHAAIAA9ACAAJABTAGMAcgBlAGUAbgAuAFQAbwBwAAoAIwAgAEMAcgBlAGEAdABlACAAYgBpAHQAbQBhAHAAIAB1AHMAaQBuAGcAIAB0AGgAZQAgAHQAbwBwAC0AbABlAGYAdAAgAGEAbgBkACAAYgBvAHQAdABvAG0ALQByAGkAZwBoAHQAIABiAG8AdQBuAGQAcwAKACQAYgBpAHQAbQBhAHAAIAA9ACAATgBlAHcALQBPAGIAagBlAGMAdAAgAFMAeQBzAHQAZQBtAC4ARAByAGEAdwBpAG4AZwAuAEIAaQB0AG0AYQBwACAAJABXAGkAZAB0AGgALAAgACQASABlAGkAZwBoAHQACgAjACAAQwByAGUAYQB0AGUAIABHAHIAYQBwAGgAaQBjAHMAIABvAGIAagBlAGMAdAAKACQAZwByAGEAcABoAGkAYwAgAD0AIABbAFMAeQBzAHQAZQBtAC4ARAByAGEAdwBpAG4AZwAuAEcAcgBhAHAAaABpAGMAcwBdADoAOgBGAHIAbwBtAEkAbQBhAGcAZQAoACQAYgBpAHQAbQBhAHAAKQAKACMAIABDAGEAcAB0AHUAcgBlACAAcwBjAHIAZQBlAG4ACgAkAGcAcgBhAHAAaABpAGMALgBDAG8AcAB5AEYAcgBvAG0AUwBjAHIAZQBlAG4AKAAkAEwAZQBmAHQALAAgACQAVABvAHAALAAgADAALAAgADAALAAgACQAYgBpAHQAbQBhAHAALgBTAGkAegBlACkACgAjACAAUwBhAHYAZQAgAHQAbwAgAGYAaQBsAGUACgAkAGIAaQB0AG0AYQBwAC4AUwBhAHYAZQAoACQARgBpAGwAZQBOAGEAbQBlACkAIAAKAHcAcgBpAHQAZQAtAGgAbwBzAHQAIAAiAHQAcgB1AGUAIgAKAH0ACgBDAGEAdABjAGgAIAB7AAoAdwByAGkAdABlAC0AaABvAHMAdAAgACIAZgBhAGwAcwBlACIACgB9AA=="

#Default primary screenShot via Powershell
def screenShotPs():
	execScreenPs = subprocess.Popen(["powershell.exe", '-EncodedCommand', scriptPs], stdout=subprocess.PIPE)
	resScreenPs = execScreenPs.communicate()[0].decode("utf-8").split('\n')[0]
	if (resScreenPs == "true"):
		return True
	else:
		return False

#ScreenShot called if default is not working
def screenShot():
	fileName = datetime.datetime.now().strftime("%d-%m-%Y~%H-%M-%S") + ".png"
	pic = pyautogui.screenshot()
	pic.save(fileName)