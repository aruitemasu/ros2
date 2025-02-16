#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Katsumi Sunahara
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

rclpy.init()
node = Node("tax_litener")


def cb(msg):
    data = msg.data.split(":")
    year = int(data[0])
    rate = int(data[1])
    note = data[2]
    if "増税" in note:
        node.get_logger().info(f"{year}年に消費税が{rate}%に上がりました（{note}）。")
    elif "そのまま" in note:
        node.get_logger().info(f"{year}年は消費税が{rate}%のままです。")
    else:
        node.get_logger().info(f"{year}年に消費税が{rate}%になりました（{note}）。")


def main():
    node.create_subscription(String, "tax_info", cb, 10)
    rclpy.spin(node)
