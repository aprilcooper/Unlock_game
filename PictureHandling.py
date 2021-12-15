# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 17:36:30 2021

@author: April Miksch
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

class Picture:
    
    def __init__(self):
        self.imgs = {}
        self.figs = {}
        self.pic_path = None
        self.scenario = None
        
        
    def read_scenario_file(self, scenario_file):
       
        path = os.path.split(scenario_file)
        print(path)
        self.pic_path=path[0]
        with open(scenario_file) as f:
            for line in f:
                key, value =  line.split()
                self.imgs[key] = value
        
    def open(self, pics, idx=None):
                     
       if isinstance(pics, int):
           #if pics not in self.figs:
            plot = plt.figure(pics)
            plt.axis('off')
            plt.tick_params(axis='both', left='off', top='off', right='off', 
                            bottom='off', labelleft='off', labeltop='off', 
                            labelright='off', labelbottom='off')
            self.figs[pics] = plot 
            img_path = self.imgs[str(pics)]
            img_path = os.path.join(self.pic_path, img_path)
            img = mpimg.imread(img_path)
            plt.imshow(img)
            plt.show()
           
        
       elif isinstance(pics, str):
           #if pics not in self.figs:
            plot = plt.figure(idx)
            plt.axis('off')
            plt.tick_params(axis='both', left='off', top='off', right='off', 
                            bottom='off', labelleft='off', labeltop='off', 
                            labelright='off', labelbottom='off')
            self.figs[pics] = plot
            img_path = self.imgs[str(pics)]
            img_path = os.path.join(self.pic_path, img_path)
            img = mpimg.imread(img_path)
            plt.imshow(img)
            plt.show()
           

    def close(self, pics):
        plot = self.figs[pics]
        plt.close(plot)
        self.figs.pop(pics)
        
        
                
            
