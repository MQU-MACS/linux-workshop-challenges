#!/bin/bash

# Iterate through all home folders and check if /home/<user>/editor/options.txt exists and contains "unlock_flag=True". Allow read permission when True.

for d in /home/*/ ; do
	options_file="$d"editor/options.txt
  if test -f $options_file; then
		case `grep "unlock_flag=True" "$options_file" >/dev/null; echo $?` in
		  0)
		    # code if found
				chmod 666 "$d"editor/flag.txt
		    ;;
		  *)
		    # code if an error occurred or not found
				echo "unlock_flag=False" > $options_file
		    ;;
		esac
 	fi
done
