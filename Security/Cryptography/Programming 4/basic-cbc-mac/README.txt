The aes* files just provide an implementation of AES. You should not
need to look at these files to do the assignment.

cbcmac.* implements a rudimentary version of basic CBC-MAC. Messages are
padded out to a multiple of the block length by appending sufficiently
many 0 bytes. Real-world implementations of (secure versions of) CBC-MAC
can handle arbitrary length messages, but we don't bother with this here.

mac.c contains wrapper code for a server that receives a 2-block
message, computes the (basic) CBC-MAC for that message using a fixed,
unknown key k, and returns the result.

vrfy.c contains wrapper code for a server that receives a message and
a tag, verifies whether the tag is correct (using the same key k), and
returns 1 or 0 accordingly. Note that arbitrary length messages are
accepted here. NOTE: You do not need to interact with the verification
routine for this assignment, but it allows you to check your answer.

sample.* contains code (in C, Ruby, and Python) demonstrating how to
write code for sending some message to obtain a tag, and for verifying
a candidate message/tag pair.
