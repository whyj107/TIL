using System;
using System.Collections.Generic;
using System.IO;
using System.Security.AccessControl;
using System.Windows;

namespace Test
{
    /// <summary>
    /// MainWindow.xaml에 대한 상호 작용 논리
    /// </summary>
    public partial class MainWindow : Window
    {
        /*
         * 1번 실행하는데 좀 오래 걸린다... 왜일까
         http://omegacoder.com/?p=63
         https://duehd88.tistory.com/entry/SHDocVw%EB%A1%9C-InternetExplorer-%EA%B0%9D%EC%B2%B4-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0
         
         2번 이것도 실행하는데 오래 걸림
        https://stackoverflow.com/questions/5708434/how-to-use-shell32-within-a-c-sharp-application/18894720
        https://social.msdn.microsoft.com/Forums/en-US/4ea6f03f-aee8-4a09-af0d-216e51a179de/how-do-i-detect-if-a-window-a-directory-window-is-open-in-windows-explorer-and-then-close-it?forum=vbgeneral
         
         3번 아직 이해 못했움 - WindowInformation.cs 여기꺼임
        https://stackoverflow.com/questions/4717667/how-do-i-find-all-windows-using-c

        4번 Lock Folder로 검색했음 뭔가 되긴하는데 내가 생각하는 그 방향은 아님
        https://stackoverflow.com/questions/4198048/how-to-lock-folder-in-c-sharp

        5번을 응용하면 될 것 같다.
        https://www.codeproject.com/Articles/20880/Folder-protection-for-Windows-using-Csharp-and-con

         */

        #region 5번
        public string status;
        string[] arr;
        private string _pathkey;
        #endregion
        public MainWindow()
        {
            InitializeComponent();

            //4번
            /*
            string folderPath = @"주소 넣자";
            string adminUserName = Environment.UserName;
            DirectorySecurity ds = Directory.GetAccessControl(folderPath);
            FileSystemAccessRule fsa = new FileSystemAccessRule(adminUserName, FileSystemRights.FullControl, AccessControlType.Deny);
            ds.AddAccessRule(fsa);
            Directory.SetAccessControl(folderPath, ds);
            MessageBox.Show("Locked");

            ds.RemoveAccessRule(fsa);
            Directory.SetAccessControl(folderPath, ds);
            MessageBox.Show("UnLocked");
            */

            arr = new string[6];
            status = string.Empty;
            arr[0] = ".{2559a1f2-21d7-11d4-bdaf-00c04f60b9f0}";
            arr[1] = ".{21EC2020-3AEA-1069-A2DD-08002B30309D}";
            arr[2] = ".{2559a1f4-21d7-11d4-bdaf-00c04f60b9f0}";
            arr[3] = ".{645FF040-5081-101B-9F08-00AA002F954E}";
            arr[4] = ".{2559a1f1-21d7-11d4-bdaf-00c04f60b9f0}";
            arr[5] = ".{7007ACC7-3202-11D1-AAD2-00805FC1270E}";

            Test();
        }

        public string pathkey
        {
            get { return _pathkey; }
            set { _pathkey = value; }
        }

        private void Test()
        {
            status = arr[0];

            DirectoryInfo d = new DirectoryInfo(@"D:\c#");
            string selectedpath = d.Parent.FullName + d.Name;
            
        }

        private Boolean setpassword(string path)
        {
            frmPassword p = new frmPassword();
            p.path = path;
            p.ShowDialog();
            return true;
        }
    }
}
