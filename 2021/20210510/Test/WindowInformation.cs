using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Runtime.InteropServices;

namespace Test
{
    public class WindowInformation
    {
        #region Constructor
        public WindowInformation() { }
        #endregion

        #region Properties
        public string Caption = string.Empty;

        public string Class = string.Empty;

        public List<WindowInformation> ChildWindows = new List<WindowInformation>();

        [DllImport("user32")]
        private static extern int GetWindowThreadProcessId(IntPtr hWnd, out int processId);

        public override string ToString()
        {
            return "Window " + this.Handle.ToString() + " \"" + this.Caption + "\" " + this.Class;
        }

        public List<IntPtr> ChildWindowHandles
        {
            get
            {
                try
                {
                    var handles = from c in this.ChildWindows.AsEnumerable()
                                  select c.Handle;
                    return handles.ToList<IntPtr>();
                }
                catch
                {
                    return null;
                }
            }
        }

        public IntPtr Handle;

        public WindowInformation Parent { get; set; }

        public IntPtr ParentHandle
        {
            get
            {
                if (this.Parent != null) return this.Parent.Handle;
                else return IntPtr.Zero;
            }
        }

        public Process Process
        {
            get
            {
                try
                {
                    int processID = 0;
                    GetWindowThreadProcessId(this.Handle, out processID);
                    return Process.GetProcessById(processID);
                }
                catch{ return null; }
            }
        }

        public List<WindowInformation> SiblingWindows = new List<WindowInformation>();

        public List<IntPtr> SiblingWindowHandles
        {
            get
            {
                try
                {
                    var handles = from s in this.SiblingWindows.AsEnumerable()
                                  select s.Handle;
                    return handles.ToList<IntPtr>();
                }
                catch
                {
                    return null;
                }
            }
        }

        public int ThreadID
        {
            get
            {
                try
                {
                    int dummy = 0;
                    return GetWindowThreadProcessId(this.Handle, out dummy);
                }
                catch{ return -1; }
            }
        }
        #endregion
    }
}