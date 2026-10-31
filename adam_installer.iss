; Inno Setup Script for ADAM — Personal AI Assistant
; Developed by avsco (https://avsco-4mdkvr2m1-park-ease3.vercel.app/index.html)

#define MyAppName "ADAM"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "avsco"
#define MyAppURL "https://avsco-4mdkvr2m1-park-ease3.vercel.app/index.html"
#define MyAppExeName "ADAM.exe"
#define MyAppSourceDir "C:\Users\Shravan\Downloads\Compressed\Mark-LIII-main\Mark-LIII-main\dist\ADAM"
#define MyOutputDir "E:\APK Files"

[Setup]
AppId={{5E3B21E9-4B52-4D9E-A6C1-729B35E994D8}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={localappdata}\Programs\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
OutputDir={#MyOutputDir}
OutputBaseFilename=ADAM-Setup-1.0.0
SetupIconFile=C:\Users\Shravan\Downloads\Compressed\Mark-LIII-main\Mark-LIII-main\config\adam.ico
Compression=lzma2/ultra64
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=lowest
DisableProgramGroupPage=yes
CloseApplications=force
CloseApplicationsFilter=*.exe
RestartApplications=no

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: checkedonce

[Files]
Source: "{#MyAppSourceDir}\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\Shravan\Downloads\Compressed\Mark-LIII-main\Mark-LIII-main\config\adam.ico"; DestDir: "{app}\config"; Flags: ignoreversion

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\Uninstall {#MyAppName}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: filesandordirs; Name: "{app}"

[Code]
function InitializeUninstall(): Boolean;
var
  ResultCode: Integer;
begin
  // Terminate ADAM if it is running in background / system tray
  Exec('taskkill.exe', '/F /IM ADAM.exe /T', '', SW_HIDE, ewWaitUntilTerminated, ResultCode);
  Sleep(500);
  Result := True;
end;
