rm_excessive_files - utility for removing excessive files in a current dirrectory. File names should be organized by specific pattern.

use case:   supose you have files in a directory, e.g.:
        fileStorage4_1c_all20240316030000.rar
        fileStorage4_1c_all20240323030000.rar
        fileStorage4_1c_all20240330030000.rar
        fileStorage4_1c_dif20240311230001.rar
        fileStorage4_1c_dif20240312230001.rar
        fileStorage4_1c_dif20240313230000.rar
        fileStorage4_1c_dif20240314230000.rar
        fileStorage4_1c_dif20240318230000.rar
        fileStorage4_1c_dif20240319230001.rar
        fileStorage4_1c_dif20240320230001.rar
        fileStorage4_1c_dif20240327230000.rar
        fileStorage4_1c_dif20240401230001.rar
        fileStorage4_1c_dif20240402230001.rar
        fileStorage4_1c_dif20240403230001.rar

        All of this files have the same name pattern: in this case the pattern is "fileStorage4_1c" followed by suffix "_all" or "_dif", followed by numbers or other chosen sequence. This sequence should make cronological sence, when sorted alphabetically. Files also have endings strictly equals to ".rar".

        1. Utility finds the oldest (sorted by name) files with suffix "_all" and

        deletes all other files with suffix "_all" but this oldest file

        2. Utility finds files with suffix "_dif", with files that are 'older' then oldest file from step 1.

        * - for the security consideration utility only works in a curent directory with which utility was executed.

usage: rm_excessive_files.exe <filepattern>
        if <filepattern> is omitted utility uses "fileStorage4_1c" pattern.

Author: Kobylin Pavel (c) 2024
