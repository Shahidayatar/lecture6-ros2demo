import rclpy
from nav_msgs.msg import Odometry
from rclpy.node import Node


class OdomMonitor(Node):
    def __init__(self) -> None:
        super().__init__('odom_monitor')
        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10,
        )

    def odom_callback(self, msg: Odometry) -> None:
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        linear_x = msg.twist.twist.linear.x
        angular_z = msg.twist.twist.angular.z
        self.get_logger().info(
            f'x={x:.3f}, y={y:.3f}, linear.x={linear_x:.3f}, angular.z={angular_z:.3f}'
        )


def main(args=None) -> None:
    rclpy.init(args=args)
    node = OdomMonitor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
