using System;

namespace Verwalten
{
    public static class CApplication
    {
        public static string progname { get; set; }
        public static int progvers { get; set; }
        public static string connstr { get; set; }
        public static string DokuDir { get; set; }
        public static string VorlagenDir { get; set; }
        public static string VorlagenKfzDir { get; set; }
        public static string TempDir { get; set; }
        public static int dbVersion { get; set; }
        public static string userName { get; set; }
        public static DateTime UserLoginTime { get; set; }

        public static int aktJahr { get; set; }
        public static string FibuPath { get; set; }
        public static int ErlKto { get; set; }

    }
}



