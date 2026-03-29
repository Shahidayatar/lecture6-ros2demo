import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node


class CircleMotion(Node):
    def __init__(self) -> None:
        super().__init__('circle_motion')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.publish_velocity)  # 10 Hz

    def publish_velocity(self) -> None:
        msg = Twist()
        msg.linear.x = 0.3
        msg.angular.z = 0.5
        self.publisher.publish(msg)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = CircleMotion()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
