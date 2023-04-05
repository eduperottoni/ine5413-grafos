CC = g++
CFLAGS = -g -Wall -W -ansi -pedantic -std=c++17
SRC_DIR = src
INCLUDES_CC = ${wildcard ./${SRC_DIR}/*.cc}
OUT = ${OUT_DIR}/main
RM= rm -rf
OUT_DIR=build

# Compiling
all: clean mk_dir
	@ echo ${INCLUDES_CC}
	@ echo 'Building executable file ${OUT}'
	@ ${CC} ${CFLAGS} ${INCLUDES_CC} -o ${OUT}
	@ echo 'Executable file ${OUT} created!'

# Checking using valgrind
# --leak-check=<no|yes|summary|full>
# --show-leak-kinds=all
check:
	valgrind  --leak-check=summary --show-leak-kinds=all ${OUT}

# Removing build directory
clean:
	@ echo ''${OUT_DIR}' dir deleted!'
	@ ${RM} ${OUT_DIR}

# Running program
run:
	@ ./${OUT}

# Making dir
mk_dir:
	@ mkdir -p ${OUT_DIR}
	@ echo ''${OUT_DIR}' dir created!'

#This submission command was copied from INE5410 exercises
submission: clean
	@SUBNAME=$$(basename "$$(pwd)"); \
		echo cd ..\; tar zcf "$$SUBNAME.tar.gz" "$$SUBNAME"
	@SUBNAME=$$(basename "$$(pwd)"); \
		cd ..; \
		rm -fr "$$SUBNAME.tar.gz"; \
		tar zcf "$$SUBNAME.tar.gz" "$$SUBNAME"
	@echo "Criado pacote \"$$(pwd).tar.gz\" para submissão"