OPENQASM 2.0;
include "qelib1.inc";

gate gate_Oracle q0,q1,q2,q3,q4,q5,q6,q7,q8,q9 {
    x q0;
    x q1;
    x q4;
    x q5;
    x q6;
    x q8;
    cx q0,q9;
    cx q1,q9;
    cx q2,q9;
    cx q3,q9;
    cx q4,q9;
    cx q5,q9;
    cx q6,q9;
    cx q7,q9;
    cx q8,q9;
    x q0;
    x q1;
    x q4;
    x q5;
    x q6;
    x q8;
}

qreg q[10];
creg c[9];

x q[9];
h q[9];

h q[0];
h q[1];
h q[2];
h q[3];
h q[4];
h q[5];
h q[6];
h q[7];
h q[8];

gate_Oracle q[0],q[1],q[2],q[3],q[4],q[5],q[6],q[7],q[8],q[9];

h q[0];
h q[1];
h q[2];
h q[3];
h q[4];
h q[5];
h q[6];
h q[7];
h q[8];

barrier q[0],q[1],q[2],q[3],q[4],q[5],q[6],q[7],q[8],q[9];

measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
measure q[3] -> c[3];
measure q[4] -> c[4];
measure q[5] -> c[5];
measure q[6] -> c[6];
measure q[7] -> c[7];
measure q[8] -> c[8];
