#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 15:26:27 2022
Modified on Fri Mar 11 15:26:27 2022
@author: An Nguyen

Description
------------
"""

# Part 1 - Histogram the data

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(1,figsize=(6,6))
fig.clf()
axes = [fig.add_subplot(321),\
        fig.add_subplot(322),\
        fig.add_subplot(323),\
        fig.add_subplot(324),\
        fig.add_subplot(325),\
        fig.add_subplot(326)]

data = np.loadtxt('refractionData.txt',skiprows=3)

a1 = data[0]
a2 = data[1]
a3 = data[2]
a4 = data[3]
a5 = data[4]
a6 = data[5]

axes[0].hist(a1,range=(-10,50),bins=10)
axes[0].set_title('alpha = 10',fontsize=10)
axes[0].set_xlabel('beta(deg.)')
axes[1].hist(a2,range=(-10,50),bins=10)
axes[1].set_title('alpha = 20',fontsize=10)
axes[1].set_xlabel('beta(deg.)')
axes[2].hist(a3,range=(-10,50),bins=10)
axes[2].set_title('alpha = 30',fontsize=10)
axes[2].set_xlabel('beta(deg.)')
axes[3].hist(a4,range=(-10,50),bins=10)
axes[3].set_title('alpha = 40',fontsize=10)
axes[3].set_xlabel('beta(deg.)')
axes[4].hist(a5,range=(-10,50),bins=10)
axes[4].set_xlabel('beta(deg.)')
axes[4].set_title('alpha = 50',fontsize=10)
axes[5].hist(a6,range=(-10,50),bins=10)
axes[5].set_title('alpha = 60',fontsize=10)
axes[5].set_xlabel('beta(deg.)')



#%%

# Part 2 - Table of measurements

b1 = np.radians(a1)
b2 = np.radians(a2)
b3 = np.radians(a3)
b4 = np.radians(a4)
b5 = np.radians(a5)
b6 = np.radians(a6)

# std of mean = std/sqrt(N) where N is # of elements

m1 = np.mean(b1)
unc1 = np.std(b1)/4

m2 = np.mean(b2)
unc2 = np.std(b2)/4

m3 = np.mean(b3)
unc3 = np.std(b3)/4

m4 = np.mean(b4)
unc4 = np.std(b4)/4

m5 = np.mean(b5)
unc5 = np.std(b5)/4

m6 = np.mean(b6)
unc6 = np.std(b6)/4

def f(x):
    return np.sin(x)

sm1 = f((m1))
sm2 = f((m2))
sm3 = f((m3))
sm4 = f((m4))
sm5 = f((m5))
sm6 = f((m6))

sunc1 = f(unc1)
sunc2 = f(unc2)
sunc3 = f(unc3)
sunc4 = f(unc4)
sunc5 = f(unc5)
sunc6 = f(unc6)

sa1 = f(10)
sa2 = f(20)
sa3 = f(30)
sa4 = f(40)
sa5 = f(50)
sa6 = f(60)


# Table

print('|  a  |  sin(a)  |    b    |  sin(b) | std sin(b) |')
print(f"|  10 |  {sa1:.3f}  |  {m1:.3f}  |  {sm1:.3f}  |   {sunc1:.3f}    |")
print(f"|  20 |   {sa2:.3f}  |  {m2:.3f}  |  {sm2:.3f}  |   {sunc2:.3f}    |")
print(f"|  30 |  {sa3:.3f}  |  {m3:.3f}  |  {sm3:.3f}  |   {sunc3:.3f}    |")
print(f"|  40 |   {sa4:.3f}  |  {m4:.3f}  |  {sm4:.3f}  |   {sunc4:.3f}    |")
print(f"|  50 |  {sa5:.3f}  |  {m5:.3f}  |  {sm5:.3f}  |   {sunc5:.3f}    |")
print(f"|  60 |  {sa6:.3f}  |  {m6:.3f}  |  {sm6:.3f}  |   {sunc6:.3f}    |")



#%%

# Part 3 - Snells law plot and fit

import scipy.stats as st

fig = plt.figure(2,figsize=(6,6))
fig.clf()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

sinA = np.array([sa1,sa2,sa3,sa4,sa5,sa6])
sinB = np.array([sm1,sm2,sm3,sm4,sm5,sm6])
uncB = np.array([sunc1,sunc2,sunc3,sunc4,sunc5,sunc6])


ax1.plot(sinA,sinB)
ax1.errorbar(sinA,sinB,uncB,fmt='ok')

def snell(a,n):
    return a/n

n = np.linspace(1.0,1.5,21)

for i in range(len(n)):
    if i%2 == 0: ax1.plot(sinA,snell(sinA,n[i]))
    
chisqvalues = np.zeros(len(n))

for i in range(len(chisqvalues)):
    chisqvalues[i] = np.sum((sinB-snell(sa1,n[i]))**2/uncB**2)
    
ax2.plot(n,chisqvalues,'ok-')
ax2.set_xlabel('slope (n)',fontsize=16)
ax2.set_ylabel('$\\chi^2$', fontsize=16)
pvalue = st.chi2.sf(chisqvalues,1)

chi2min = chisqvalues.min()
ax2.hlines(chi2min,1.0,1.5)
ax2.hlines(chi2min+1.0,1.0,1.5)
ax2.vlines(1.092,0.0,chi2min+1,ls='--')
ax2.vlines(1.35,0.0,chi2min+1,ls='--')
ax2.vlines(1.22,0.0,chi2min+1)
ax2.set_xlim(1.0,1.5)
ax2.set_xticks(np.linspace(1.0,1.5,11))
ax2.set_title('$\\chi^2$ vs slope',fontsize=10)





######################################################
