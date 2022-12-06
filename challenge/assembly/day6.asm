; Sections:
section .data
  text_part1: db "Part 1: "
  text_part2: db "Part 2: "

section .bss
  input: resb 4100
  digitSpace resb 100
  digitSpacePos resb 8

section .text
  global _start

; Functions:

printRAX: ; Print number stored in rax as decimal
  mov rcx, digitSpace
  mov rbx, 10
  mov [rcx], rbx
  inc rcx
  mov [digitSpacePos], rcx
  
.loop:
  mov rdx, 0
  mov rbx, 10
  div rbx
  push rax
  add rdx, 48

  mov rcx, [digitSpacePos]
  mov [rcx], dl
  inc rcx
  mov [digitSpacePos], rcx

  pop rax
  cmp rax, 0
  jne .loop

.loop2:
  mov rcx, [digitSpacePos]

  mov rax, 1
  mov rdi, 1
  mov rsi, rcx
  mov rdx, 1
  syscall

  mov rcx, [digitSpacePos]
  dec rcx
  mov [digitSpacePos], rcx

  cmp rcx, digitSpace
  jge .loop2

  ret

check_unique:
  mov r11, rbx ; store starting offset
  mov rax, rbx ; current char index we are checking if unique
  mov r10, 1 ; return value

.outer_loop:
  cmp rax, rcx
  je .real_end

.loop:
  cmp rbx, rcx
  je .end
  
  cmp rbx, rax
  je .inc


  mov r8b, byte [rdi + rbx]
  mov r9b, byte [rdi + rax]
  cmp r8b, r9b
  je .not_unique

.inc:
  inc rbx
  jmp .loop

.not_unique:
  mov r10, 0
  jmp .real_end

.end:
  inc rax
  mov rbx, r11
  jmp .outer_loop


.real_end:
  mov rax, r10
  mov rbx, r11
  ret


find_unique: ; find end of unique string at length rcx
  mov rbx, 0 ; loop index
.iter:
  mov rdi, input ; string pointer
  call check_unique
  cmp rax, 1
  jne .continue
  ret
.continue:  

  inc rbx
  inc rcx
  jmp .iter

_start:
  mov rax, 0
  mov rdi, 0
  mov rsi, input
  mov rdx, 4100
  syscall

  mov rcx, 4 ; loop end
  call find_unique
  push rcx

  mov rax, 1
  mov rdi, 1
  mov rsi, text_part1
  mov rdx, 8
  syscall

  pop rax
  call printRAX
  
  mov rcx, 14 ; loop end
  call find_unique
  push rcx

  mov rax, 1
  mov rdi, 1
  mov rsi, text_part2
  mov rdx, 8
  syscall

  pop rax
  call printRAX

  mov rax, 60
  mov rdi, 0
  syscall


