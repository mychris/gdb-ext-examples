
CC = clang

all: redirect-dump

redirect-dump: redirect-dump.c
	$(CC) -O0 -ggdb3 redirect-dump.c -o redirect-dump

clean:
	$(RM) redirect-dump

.PHONY: all clean
