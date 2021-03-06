import argparse

parser = argparse.ArgumentParser(description='pix2pix in PyTorch')
parser.add_argument('--phase', required=True, help='Pix2Pix in training / testing phase')

parser.add_argument('--epochs', type=int, default=200, help='training epochs')
parser.add_argument('--batchSize', type=int, default=1, help='batch size of data')
parser.add_argument('--imageSize', type=int, default=256, help='the height / width of the input image')

parser.add_argument('--input_nc', type=int, default=3, help='input image channels')
parser.add_argument('--output_nc', type=int, default=3, help='output image channels')
parser.add_argument('--ngf', type=int, default=64, help='generator filters in first conv layer')
parser.add_argument('--ndf', type=int, default=64, help='discriminator filters in first conv layer')
parser.add_argument('--lr', type=float, default=0.0002, help='learning rate, default=0.0002')
parser.add_argument('--beta1', type=float, default=0.5, help='beta1 for adam. default=0.5')
parser.add_argument('--lamb', type=int, default=100, help='weight on L1 term in objective')

parser.add_argument('--save_freq', type=int, default=5, help='how often to saving model and results')
parser.add_argument('--log_freq', type=int, default=50, help='how often of logging about batch')

parser.add_argument('--dataset', default='facades', help="dataset used in pix2pix")
parser.add_argument('--direction', default='AtoB', help="direction of image translation")
parser.add_argument('--folderA', default='', help="folder of images used as image A")
parser.add_argument('--folderB', default='', help="folder of images used as image B")

parser.add_argument('--log_dir', default='./logs', help="path output model and logging stuffs")
parser.add_argument('--result_dir', default='./results', help="path output stuffs")
parser.add_argument('--netG', default='', help="path to netG (to continue training)")
parser.add_argument('--netD', default='', help="path to netD (to continue training)")

parser.add_argument('--workers', type=int, default=4, help='number of data loading workers')
parser.add_argument('--ngpu', type=int, default=1, help='number of GPUs to use')
parser.add_argument('--cuda', action='store_true', help='enables cuda')
